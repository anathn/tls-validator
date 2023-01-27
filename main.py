from tlsscan import load_domains, retrieve_certs, process_domains
from module_htmldump import dump_html
import sys, os

def filter_troubles(domain_data):
    troubled_domains = {}
    for domain in domain_data:
        if domain_data[domain]['messages']:
            troubled_domains[domain] = domain_data[domain]
    return troubled_domains

def create_html(filename, domain_data):
    output = dump_html(domain_data)
    with open(filename, 'w') as f:
        f.write(output)

def main(filename):
    domains = load_domains(filename)
    certs = retrieve_certs(domains)
    # all domains scanned
    domain_data = process_domains(certs, expire_warning_days=14)
    # filter out the ones that:
    # Are expiring
    # Have expired
    # Have issues (invalid names, etc)
    troubled_domains = filter_troubles(domain_data)

    # dump all domains to html page
    create_html('all_domains.html', domain_data)
    # dump troubled domains to html page
    create_html('troubles.html', troubled_domains)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if  not os.path.exists(filename):
            print(f"ERROR:  {filename} does not exist or is invalid.")
            exit()
    else:
        filename = "sample-file.txt"
    main(filename)

