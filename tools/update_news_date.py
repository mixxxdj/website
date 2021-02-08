#!/usr/bin/env python3
import argparse
import datetime
import os
import re
import subprocess
import sys

RE_POST_DATE = re.compile(r"^date:\s+(.*)$", flags=re.MULTILINE)
RE_POST_STATUS = re.compile(r"\nstatus:[ \t]+draft\n")


def find_commit_that_added_file(path: str, format: str = "oneline"):
    lines = subprocess.check_output(
        (
            "git",
            "log",
            "-m",
            "--follow",
            "--diff-filter=A",
            f"--pretty={format}",
            "--",
            path,
        ),
        encoding="utf-8",
    ).splitlines()
    return lines[-1].strip()


def find_merge_commit_to_branch(commit: str, branch: str):
    ancestry_path = subprocess.check_output(
        (
            "git",
            "rev-list",
            f"{commit}..{branch}",
            "--ancestry-path",
        ),
        encoding="utf-8",
    ).splitlines()

    first_parent = subprocess.check_output(
        (
            "git",
            "rev-list",
            f"{commit}..{branch}",
            "--first-parent",
        ),
        encoding="utf-8",
    ).splitlines()

    common_commits = reversed(
        [commit for commit in ancestry_path if commit in first_parent]
    )
    return next(common_commits)


def show_commit(commit: str, format: str = "format:%H"):
    return subprocess.check_output(
        (
            "git",
            "show",
            "--no-patch",
            "--no-notes",
            f"--pretty={format}",
            commit,
        ),
        encoding="utf-8",
    ).partition("\n")[0]


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="+", help="Path to news/ directory")
    parser.add_argument(
        "-b",
        "--branch",
        required=True,
        help="Branch to check the merge date of",
    )
    parser.add_argument(
        "-n",
        "--dry-run",
        action="store_true",
        help="Do not actually change files",
    )
    args = parser.parse_args(argv)

    branch = args.branch

    for path in args.path:
        with os.scandir(path=path) as it:
            for entry in it:
                if not entry.is_file():
                    continue

                matchobj = re.match(
                    r"^([0-9X]{4})-XX-XX-(?P<title>.*)$", entry.name
                )
                if not matchobj:
                    continue

                filepath = os.path.join(path, entry.name)
                print(f"Found file: {filepath}")
                commit, _, commit_msg = find_commit_that_added_file(
                    filepath
                ).partition(" ")
                print(f"  Added in commit: {commit}")
                print(f"    {commit_msg}")
                try:
                    merge_commit = find_merge_commit_to_branch(commit, branch)
                except StopIteration:
                    print("  Skipping because the merge commit was not found!")
                    continue
                print(f"  Merged to {branch} in commit: {merge_commit}")
                merge_datestr, _, merge_msg = show_commit(
                    merge_commit, format="%cI %s"
                ).partition(" ")
                print(f"    {merge_msg}")
                merge_datetime = datetime.datetime.fromisoformat(merge_datestr)
                print(f"  Merge date: {merge_datetime}")

                post_date = merge_datetime.strftime("%Y-%m-%d %H:%M:%S")

                title = matchobj.group("title")
                date = merge_datetime.strftime("%Y-%m-%d")
                new_filepath = os.path.join(path, f"{date}-{title}")
                print(f"  New filename: {new_filepath}")

                if os.path.exists(new_filepath):
                    print("  Skipping because new filename already exists!")
                    print("")
                    continue

                with open(
                    filepath, mode="r", encoding="utf-8", newline="\n"
                ) as fp:
                    header, sep, body = fp.read().partition("\n\n")
                    if not RE_POST_STATUS.findall(header):
                        print("  Skipping because post is not a draft!")

                    header = RE_POST_STATUS.sub("\n", header)

                    if RE_POST_DATE.findall(header):
                        header = RE_POST_DATE.sub(f"date: {post_date}", header)
                    else:
                        header += f"\ndate: {post_date}"

                print("")

                if args.dry_run:
                    continue

                with open(
                    filepath, mode="w", encoding="utf-8", newline="\n"
                ) as fp:
                    fp.seek(0)
                    fp.write(header)
                    fp.write(sep)
                    fp.write(body)
                    fp.truncate()

                os.rename(filepath, new_filepath)


if __name__ == "__main__":
    sys.exit(main())
