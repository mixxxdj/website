#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


def parse_redirects(filepath):
    rules = []
    with open(filepath) as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            rule = parse_redirect_line(line)
            if rule:
                rules.append(rule)
            else:
                print(
                    f"Warning: Could not parse line {i}: {line}",
                    file=sys.stderr,
                )
    return rules


def parse_redirect_line(line):
    parts = line.split()
    if len(parts) < 3:
        return None

    status_raw = parts[-1]
    status_match = re.match(r"^(\d{3})(!)?$", status_raw)
    if not status_match:
        return None
    status = int(status_match.group(1))
    force = bool(status_match.group(2))

    before_status = parts[:-1]
    to_url = before_status[-1]
    from_parts = before_status[:-1]

    if not from_parts:
        return None

    from_pattern = from_parts[0]
    query_param_parts = from_parts[1:]

    query_params = []
    for qp in query_param_parts:
        if "=" in qp:
            key, val = qp.split("=", 1)
            query_params.append((key, val))

    return {
        "from": from_pattern,
        "to": to_url,
        "status": status,
        "force": force,
        "query_params": query_params,
    }


def redirect_to_htaccess(rule):
    lines = []
    from_pattern = rule["from"]
    to_url = rule["to"]
    status = rule["status"]
    query_params = rule["query_params"]

    if status == 404 and from_pattern == "/*":
        return [f"ErrorDocument 404 {to_url}"]

    if from_pattern.startswith(("http://", "https://")):
        url_match = re.match(r"^(https?://)?([^/]+)(/.*)?$", from_pattern)
        if url_match:
            scheme = url_match.group(1)
            host = url_match.group(2)
            from_path = url_match.group(3)
            if from_path is None:
                from_path = "/*"
            host_escaped = re.escape(host)
            lines.append(f"RewriteCond %{{HTTP_HOST}} ^{host_escaped}$ [NC]")
            if scheme == "http://":
                lines.append("RewriteCond %{HTTPS} off")
            elif scheme == "https://":
                lines.append("RewriteCond %{HTTPS} on")
        else:
            return []
    else:
        from_path = from_pattern

    from_regex_chars = []
    i = 0
    while i < len(from_path):
        ch = from_path[i]
        if ch == "*":
            from_regex_chars.append("(.*)")
        elif ch in ".+?^${}[]|\\()":
            from_regex_chars.append("\\" + ch)
        else:
            from_regex_chars.append(ch)
        i += 1
    from_regex = "".join(from_regex_chars)

    if from_regex.startswith("/"):
        from_regex = from_regex[1:]

    replacement = to_url.replace(":splat", "$1")
    base_url, _, qs = replacement.partition("?")
    if qs and re.search(r":\w+", qs):
        replacement = base_url

    flags_parts = [f"R={status}", "L"]
    if query_params:
        flags_parts.append("QSA")
    flags = ",".join(flags_parts)

    for key, val in query_params:
        escaped_key = re.escape(key)
        if val and not val.startswith(":"):
            escaped_val = re.escape(val)
            cond = f"(?:^|&){escaped_key}={escaped_val}(?:&|$)"
        else:
            cond = f"(?:^|&){escaped_key}=[^&]*(?:&|$)"
        lines.append(f"RewriteCond %{{QUERY_STRING}} {cond} [NC]")

    lines.append(f"RewriteRule ^{from_regex}$ {replacement} [{flags}]")
    return lines


def parse_netlify_headers(filepath):
    with open(filepath, "rb") as f:
        data = tomllib.load(f)

    headers_list = data.get("headers", [])
    if not isinstance(headers_list, list):
        return []

    result = []
    for entry in headers_list:
        for_val = entry.get("for", "/*")
        values = entry.get("values", {})
        if values:
            result.append({"for": for_val, "values": dict(values)})
    return result


def headers_to_htaccess(headers):
    lines = ["<IfModule mod_headers.c>"]

    for entry in headers:
        for_val = entry["for"]
        values = entry["values"]

        if for_val == "/*":
            for key, val in values.items():
                lines.append(f'  Header set {key} "{val}"')
        else:
            apache_pattern = for_val.replace("*", ".*")
            if apache_pattern.startswith("/"):
                apache_pattern = "^" + apache_pattern
            env_name = re.sub(r"[^a-zA-Z0-9_]+", "_", for_val).strip("_")
            env_var = "hdr_" + env_name if env_name else "hdr_custom"
            lines.append(
                f'  SetEnvIf Request_URI "{apache_pattern}" {env_var}'
            )
            for key, val in values.items():
                lines.append(f'  Header set {key} "{val}" env={env_var}')

    lines.append("</IfModule>")
    return lines


def strip_template_tags(content):
    out_lines = []
    for line in content.splitlines():
        stripped = line.strip()
        if stripped in (
            "{% verbatim %}",
            "{% endverbatim %}",
            "{%verbatim%}",
            "{%endverbatim%}",
        ):
            continue
        out_lines.append(line)
    return "\n".join(out_lines)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Generate .htaccess from Netlify _redirects and netlify.toml"
        )
    )
    parser.add_argument("--template", "-t", help="Base htaccess template file")
    parser.add_argument(
        "--redirects",
        "-r",
        default="content/_redirects",
        help="Path to _redirects file (default: content/_redirects)",
    )
    parser.add_argument(
        "--netlify-config",
        "-n",
        default="netlify.toml",
        help="Path to netlify.toml (default: netlify.toml)",
    )
    parser.add_argument("--output", "-o", help="Output file (default: stdout)")
    args = parser.parse_args()

    out_lines = []

    if args.template:
        template_path = Path(args.template)
        if template_path.exists():
            content = strip_template_tags(template_path.read_text())
            if content.strip():
                out_lines.append(content.rstrip())
        else:
            print(
                f"Warning: template file not found: {args.template}",
                file=sys.stderr,
            )

    if args.redirects:
        redirects_path = Path(args.redirects)
        if redirects_path.exists():
            rules = parse_redirects(args.redirects)
            redirect_lines = []
            for rule in rules:
                rule_lines = redirect_to_htaccess(rule)
                if rule_lines:
                    redirect_lines.extend(rule_lines)
                    redirect_lines.append("")
            if redirect_lines:
                if out_lines and out_lines[-1] != "":
                    out_lines.append("")
                out_lines.append("# Redirects from content/_redirects")
                out_lines.extend(redirect_lines)
        else:
            print(
                f"Warning: redirects file not found: {args.redirects}",
                file=sys.stderr,
            )

    if args.netlify_config:
        config_path = Path(args.netlify_config)
        if config_path.exists():
            headers = parse_netlify_headers(args.netlify_config)
            if headers:
                if out_lines and out_lines[-1] != "":
                    out_lines.append("")
                header_lines = headers_to_htaccess(headers)
                out_lines.extend(header_lines)
                out_lines.append("")
        else:
            print(
                f"Warning: netlify config not found: {args.netlify_config}",
                file=sys.stderr,
            )

    content = "\n".join(out_lines)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content)
    else:
        sys.stdout.write(content)
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
