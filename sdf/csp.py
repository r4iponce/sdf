"""
enumerate subdomain or url with Content-Security-Policy header.
"""

import re

import requests


def get_csp_headers(domain: str) -> str:
    """
    Fetch all subdomain
    :param domain: Domains for which we are looking for subdomains
    :return: List of found subdomains
    """
    get = requests.get(f"https://{domain}", timeout=30, allow_redirects=True)
    return get.headers["Content-Security-Policy"]


def detect_domain(word: str) -> bool:
    """
    Parse if a string is a valid domain
    :param word: source word
    :return: True if string are valid domain
    """
    return bool("." in word)


def extract_domain(domain: str) -> list[str]:
    """
    Extract valid domain for string
    :param domain: Domains for which we are looking for subdomains
    :return: List of found subdomains
    """
    headers = get_csp_headers(domain)
    separate_item = re.split(" ", headers)

    domain_list = []
    for key in separate_item:
        if detect_domain(key):
            domain_list.append(key.replace(";", ""))

    return domain_list
