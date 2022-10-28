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
args = parser.parse_args()
