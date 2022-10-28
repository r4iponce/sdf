import crtsh
import csp
from utils import print_list, remove_redundant_in_list


def get_domain_list(domain: str) -> list[str]:
    domain_list = []
    for subdomain in crtsh.quiet_output(domain):
        domain_list.append(subdomain)

    try:
        for subdomain in csp.extract_domain(domain):
            domain_list.append(subdomain)
    except KeyError:
        print("CSP error")

    return remove_redundant_in_list(domain_list)


def main() -> None:
    subdomain = get_domain_list(args.domain)
    print_list(subdomain)


if __name__ == "__main__":
    from command_options import args

    main()
