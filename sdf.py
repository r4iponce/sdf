#!/usr/bin/env python3

import crtsh
import csp
from utils import print_list, remove_redundant_in_list


def get_domain_list(domain: str) -> list[str]:
    domain_list = []
    if args.crtsh and args.csp:
        raise Exception("Sorry, use minimum 1 option")

    if args.crtsh and not args.csp:
        for subdomain in csp.extract_domain(domain):
            domain_list.append(subdomain)

    if args.csp and not args.crtsh:
        for subdomain in crtsh.quiet_output(domain):
            domain_list.append(subdomain)
    else:
        for subdomain in crtsh.quiet_output(domain):
            domain_list.append(subdomain)
        try:
            for subdomain in csp.extract_domain(domain):
                domain_list.append(subdomain)
        except KeyError:
            print("Missing csp header")

    return remove_redundant_in_list(domain_list)


def main() -> None:
    subdomain = get_domain_list(args.domain)
    print_list(subdomain)


if __name__ == "__main__":
    from command_options import args

    main()
