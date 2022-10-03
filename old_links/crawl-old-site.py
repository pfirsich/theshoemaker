import argparse
import json
import re
import sys

import requests

VERBOSE = False


class Url:
    def __init__(self, url):
        self.url = url
        self.visited = False
        self.visited_from = []


def log(s):
    if not s.endswith("\n"):
        s += "\n"
    sys.stderr.write(s)


def verbose(s):
    if VERBOSE:
        log(s)


def get_next_url(visited):
    for url in visited.values():
        if not url.visited:
            return url.url
    return None


def is_absolute(link):
    return link.startswith("http:") or link.startswith("https:")


def add_link(link, visited_from, visited):
    if is_absolute(link):
        if "/theshoemaker.de" not in link:
            if "theshoemaker.de" in link:
                log("Subdomain: {}".format(link))
            return
        url = link
    elif link.startswith("/"):
        if link.startswith("//"):
            log("Weird shit: {}".format(link))
            return
        url = "https://theshoemaker.de" + link
    else:
        log("Relative: {}".format(link))
        return

    url = url.split("#")[0]
    if url not in visited:
        visited[url] = Url(url)
    visited[url].visited_from.append(visited_from)


def visit(url, visited):
    verbose("visit {}".format(url))
    resp = requests.get(url)
    content_type_blacklist = ["image/png", "image/jpeg", "image/gif"]
    verbose(resp.headers["Content-Type"])
    if resp.headers["Content-Type"] not in content_type_blacklist:
        body = resp.content.decode("utf-8")
        for href in re.findall(r"href=\"(.*?)\"", body):
            add_link(href, url, visited)
        for src in re.findall(r"src=\"(.*?)\"", body):
            add_link(src, url, visited)
    visited[url].visited = True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    global VERBOSE
    if args.verbose:
        VERBOSE = True

    next_url = "https://theshoemaker.de"
    visited = {next_url: Url(next_url)}
    while next_url:
        visit(next_url, visited)
        verbose("{}/{}".format(sum(u.visited for u in visited.values()), len(visited)))
        next_url = get_next_url(visited)

    json_data = {}
    for url, url_object in sorted(visited.items()):
        json_data[url] = url_object.visited_from

    print(json.dumps(json_data, indent=2))


if __name__ == "__main__":
    main()
