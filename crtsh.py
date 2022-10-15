#!/usr/bin/env python3

import json
import sys
from pprint import pprint

import requests


def fetch_subdomain(domain: str) -> str:
    get = requests.get(f"https://crt.sh/?q={domain}&output=json", timeout=30)
    content = json.dumps(get.json(), indent=2)
    return content


if __name__ == '__main__':
    print(pprint(fetch_subdomain(sys.argv[1])))
