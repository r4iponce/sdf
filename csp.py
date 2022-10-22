"""
enumerate subdomain or url with Content-Security-Policy header.
"""

import re

import requests


def get_csp_headers(url: str) -> str:
    get = requests.get(f"https://{url}", timeout=30, allow_redirects=True)
    return get.headers["Content-Security-Policy"]


def detect_domain(word: str) -> bool:
    return bool("." in word)


def extract_domain(domain: str) -> list[str]:
    headers = get_csp_headers(domain)
    separate_item = re.split(" ", headers)

    domain_list = []
    for key in separate_item:
        if detect_domain(key):
            domain_list.append(key.replace(";", ""))

    return domain_list
