import crtsh
import csp
from utils import remove_redundant_in_list


def main() -> None:
    domain_list = []
    if args.quiet:
        for subdomain in crtsh.quiet_output(args.domain):
            domain_list.append(subdomain)

        try:
            for subdomain in csp.extract_domain(args.domain):
                domain_list.append(subdomain)
        except KeyError:
            print("CSP error")

        domain_list = remove_redundant_in_list(domain_list)
        for item in domain_list:
            print(item)
    else:
        pass


if __name__ == "__main__":
    from command_options import args

    main()
