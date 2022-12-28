"""
Parse command line options
"""


import argparse

parser = argparse.ArgumentParser(description="Fetch subdomain based on crt.sh")

parser.add_argument(
    "-d",
    "--domain",
    help="Specify domain to search",
    type=str,
    required=True,
    dest="domain",
)

parser.add_argument(
    "--crtsh",
    help="Disable use of crt.sh API",
    dest="crtsh",
    action="store_true",
    default=False,
)

parser.add_argument(
    "--csp",
    help="Disable use CSP module",
    dest="csp",
    action="store_true",
    default=False,
)

args = parser.parse_args()
