"""
Control command line interface
"""

import sdf.crtsh
import sdf.csp
from sdf.command_options import args
from sdf.utils import print_list


def get_domain_list(domain: str) -> list[str]:
    """
    Fetch all subdomain
    :param domain: Domains for which we are looking for subdomains
    :return: List of found subdomains
    """
    domain_list = []
    if args.crtsh and args.csp:
        raise Exception("Sorry, use minimum 1 option")

    if args.crtsh and not args.csp:
        for subdomain in sdf.csp.extract_domain(domain):
            domain_list.append(subdomain)

    if args.csp and not args.crtsh:
        for subdomain in sdf.crtsh.quiet_output(domain):
            domain_list.append(subdomain)
    else:
        for subdomain in sdf.crtsh.quiet_output(domain):
            domain_list.append(subdomain)
        try:
            for subdomain in sdf.csp.extract_domain(domain):
                domain_list.append(subdomain)
        except KeyError:
            print("Missing csp header")

    return list(set(domain_list))


def main() -> None:
    """
    Command line interface
    """
    subdomain = get_domain_list(args.domain)
    print_list(list(set(subdomain)))


if __name__ == "__main__":
    main()
