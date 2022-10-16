#!/usr/bin/env python3

import re

import requests

from utils import remove_redundant_in_list


# enumerate subdomain or url with Content-Security-Policy header.


def get_csp_headers(url: str) -> str:
    get = requests.get(f"https://{url}", timeout=30, allow_redirects=True)
    return get.headers["Content-Security-Policy"]


def detect_domain(word: str) -> bool:
    return bool('.' in word)


def extract_domain(domain) -> list:
    headers = get_csp_headers(domain)
    separate_item = (re.split(' ', headers))

    domain_list = []
    for key in separate_item:
        if detect_domain(key):
            domain_list.append(key.replace(';', ''))

    return remove_redundant_in_list(domain_list)


def main():
    domain_list = extract_domain(args.domain)
    for item in domain_list:
        print(item)


if __name__ == '__main__':
    from command_options import args

    main()
