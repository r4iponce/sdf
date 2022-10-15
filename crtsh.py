#!/usr/bin/env python3

import argparse
from pprint import pprint

import requests

parser = argparse.ArgumentParser(
    description="Fetch subdomain based on crt.sh"
)
parser.add_argument('-q', '--quiet',
                    help="Only display domain",
                    action='store_true',
                    default=False,
                    dest='quiet')

parser.add_argument("-d", "--domain",
                    help="Specify domain to search",
                    type=str,
                    required=True,
                    dest="domain")
args = parser.parse_args()


def fetch_subdomain(domain: str) -> dict:
    """
    :param domain: asked domain
    :return: get json for asked domain
    """
    get = requests.get(f"https://crt.sh/?q={domain}&output=json", timeout=30)

    return get.json()


def quiet_output() -> list:
    """
    :return: only domain list.
    """
    data = fetch_subdomain(args.domain)
    subdomain_list = []
    for item in data:
        subdomain_list.append(item['name_value'])

    return remove_redundant_in_list(subdomain_list)


def remove_redundant_in_list(source_list: list) -> list:
    sorted_list = []
    for item in source_list:
        if item not in sorted_list:
            sorted_list.append(item)
    return sorted_list


def main():
    if args.quiet:
        for subdomain in quiet_output():
            print(subdomain)
    else:
        pprint(fetch_subdomain(args.domain))


if __name__ == '__main__':
    main()
