#!/usr/bin/env python3

from pprint import pprint

import requests

from utils import remove_redundant_in_list


def fetch_subdomain(domain: str) -> dict:
    """
    :param domain: asked domain
    :return: get json for asked domain
    """
    get = requests.get(f"https://crt.sh/?q={domain}&output=json", timeout=30)

    return get.json()


def quiet_output(domain: str) -> list:
    """
    :return: only domain list.
    """
    data = fetch_subdomain(domain)
    subdomain_list = []
    for item in data:
        subdomain_list.append(item['name_value'])

    return remove_redundant_in_list(subdomain_list)


def main():
    if args.quiet:
        for subdomain in quiet_output(args.domain):
            print(subdomain)
    else:
        pprint(fetch_subdomain(args.domain))


if __name__ == '__main__':
    from command_options import args

    main()
