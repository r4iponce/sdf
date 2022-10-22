"""
enumerate subdomain with certificate transparency.
"""

import requests


def fetch_subdomain(domain: str) -> dict:
    """
    :param domain: asked domain
    :return: get json for asked domain
    """
    get = requests.get(f"https://crt.sh/?q={domain}&output=json", timeout=30)

    return get.json()


def quiet_output(domain: str) -> list[str]:
    """
    :return: only domain list.
    """
    data = fetch_subdomain(domain)
    subdomain_list = []
    for item in data:
        subdomain_list.append(item["name_value"])

    return subdomain_list
