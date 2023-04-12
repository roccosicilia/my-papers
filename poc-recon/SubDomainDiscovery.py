'''
Usege:  SubDomainDiscovery --domain contoso.hack --mode amass
'''

import requests
import sys
import subprocess
import socket
import json
from shodan import Shodan

domain = sys.argv[1]
mode = sys.argv[2]
shodan_key = sys.argv[3]

### function def
def tabber(string):
    string_len = len(string)
    empty = 50 - string_len
    tab = '-'*empty
    return tab

### main program -- anass utility
if "amass" in mode:   # search subdomain via DuckDuckGo
    result = subprocess.check_output(["amass", "enum", "-passive", "-d", domain])
    #print(result.decode("utf-8"))
    subdomains = result.splitlines()

    for subdomain in subdomains:

        # gat domain info
        print("# Get domain info for {subdomain}")
        try:

            subdomain_ip = socket.gethostbyname(subdomain)
            subdomain_str = subdomain.decode("utf-8")
            tab = tabber(subdomain_str)
            # print("| {} {} | {}\t|".format(subdomain_str, tab, subdomain_ip))
            output = "| {} {} | {}\t|".format(subdomain_str, tab, subdomain_ip)

        except:

            subdomain_str = subdomain.decode("utf-8")
            tab = tabber(subdomain_str)
            # print("| {} {} | n/a \t\t|".format(subdomain_str, tab))
            output = "| {} {} | n/a \t\t|".format(subdomain_str, tab)
        
        # get shodan info
        print("# Get Shodan info for {subdomain}")
        try:

            shodan_result = subprocess.check_output(["curl", "-X", "GET", subdomain_ip])
            shodan_json = json.load(shodan_result)
            ports = shodan_json["ports"]
            output = output + " {} |".format(ports)

        except:

            output = output + " n/a | "
        
        print(output)