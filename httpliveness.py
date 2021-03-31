import requests
import socket
import argparse
from collections import defaultdict
import re

def main( website, alias ):
    ip = socket.gethostbyname(website) 
    responses = defaultdict(int)
    counter = 0
    while True:
        counter += 1
        try:
            url = re.compile(r"https?://(www\.)?")
            host = url.sub('', website).strip().strip('/')
            ip = socket.gethostbyname_ex(host)
            ip = str(ip[0] if alias else ip[2])
            r =requests.get(website,timeout=1)
            print(f"Check {website} ({ip}) response: {str(r.status_code)}")
            responses[r.status_code] += 1
        except requests.exceptions.Timeout:
            responses["timeout"] += 1
            print(f"Request timeout for {ip} {counter}")
        except:
            print(f"\n --- {website} HTTP requests statistics ---")
            output = f"{counter} HTTP requested"
            for k in responses.keys():
                output += f", {str(responses[k])} {str(k)} responses"
            print(output)
            break


# Parser
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('host', metavar='https://www.example.com')
parser.add_argument('-a', '--alias', action='store', type=bool, nargs='?', const=True, default=False, help="Returns IP or Alias")
args = parser.parse_args()

main( args.host, args.alias )