import argparse

parser = argparse.ArgumentParser(description="Fetch subdomain based on crt.sh")
parser.add_argument(
    "-q",
    "--quiet",
    help="Only display domain",
    action="store_true",
    default=False,
    dest="quiet",
)

parser.add_argument(
    "-d",
    "--domain",
    help="Specify domain to search",
    type=str,
    required=True,
    dest="domain",
)
args = parser.parse_args()
