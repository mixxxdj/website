#!/usr/bin/env python3
import importlib.util
import os
import urllib.request


def download_avatar(username):
    url = f"https://avatars.githubusercontent.com/{username}?size=60"
    with urllib.request.urlopen(url) as response:
        data = response.read()
    return data


def read_pelican_config(path):
    spec = importlib.util.spec_from_file_location("pelicanconf", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    confpath = os.path.join(os.path.dirname(__file__), "..", "pelicanconf.py")
    outpath = os.path.join(
        os.path.dirname(__file__), "..", "theme", "static", "images", "avatars"
    )
    config = read_pelican_config(confpath)
    os.makedirs(outpath, exist_ok=True)
    for author in config.AUTHOR_METADATA.values():
        username = author.get("github")
        if not username:
            continue
        filename = os.path.join(outpath, f"{username}.png")
        print(f"Downloading avatar of user {username}...")
        data = download_avatar(username)
        with open(filename, "w+b") as fp:
            fp.write(data)


if __name__ == "__main__":
    main()
