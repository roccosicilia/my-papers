'''
Usege:  SubDomainDiscovery --domain contoso.hack --mode amass
'''

import requests
import sys
import subprocess
import socket

domain =    sys.argv[1]
mode =      sys.argv[2]
#output =    sys.argv[3]

### function def
def tabber(string):
    string_len = len(string)
    if string_len >= 30:
        tab = '\t'
    elif string_len > 20 and string_len < 30:
        tab = '\t\t'
    else:
        tab = '\t'
    return tab

### main program -- anass utility
if "amass" in mode:   # search subdomain via DuckDuckGo
    result = subprocess.check_output(["amass", "enum", "-passive", "-d", domain])
    #print(result.decode("utf-8"))
    subdomains = result.splitlines()

    for subdomain in subdomains:
        try:

            subdomain_ip = socket.gethostbyname(subdomain)
            subdomain_str = subdomain.decode("utf-8")
            tab = tabber(subdomain_str)
            print("| {}{}| {}\t|".format(subdomain_str, tab, subdomain_ip))

        except:

            subdomain_str = subdomain.decode("utf-8")
            tab = tabber(subdomain_str)
            print("| {}{}]| n/a\t|".format(subdomain_str, tab))
