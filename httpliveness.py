import requests
import socket
import argparse
from collections import defaultdict
import re
import time
import json

# Main function
def main( website, alias, wait, quiet, output, method, timeout, count ):
    # Initiate variables
    responses = defaultdict(int)
    counter = 0
    # Infinite Loop
    while True:
        try:
            # Counter fun
            if count == 0:
                raise
            elif count > 0:
                count -= 1
            counter += 1

            # Cleanup URL to Hosts
            url = re.compile(r"https?://(www\.)?")
            host = url.sub('', website).strip().strip('/')
            # Get host information to display IP or CNAME
            host = socket.gethostbyname_ex(host)
            host = str(host[0] if alias else host[2])
            # HTTP Requests
            if method == "head":
                r =requests.head(website,timeout=timeout)
            elif method == "get":
                r =requests.get(website,timeout=timeout)
            # Output or not
            if not quiet:
                print(f"Check {website} ({host}) response: {str(r.status_code)}")
            responses[r.status_code] += 1
            # Added waittime - Slow requests
            time.sleep(wait)
        # Output timeouts or not    
        except requests.exceptions.Timeout:
            responses["timeout"] += 1
            if not quiet:
                print(f"Request timeout for {host} {counter}")
        # Outputs in Text or JSON
        except:
            if (output == "text"):
                print(f"\n --- {website} HTTP requests statistics ---")
                output = f"{counter} HTTP requested"
                for k in responses.keys():
                    output += f", {str(responses[k])} {str(k)} responses"
                print(output)
            elif (output == "json"):
                responses["counter"] = counter
                output = json.dumps(responses, indent = 4)  
                print(output)
            break

# Parse all the things
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('URL', help='Enter URL with the patter - http(s)://<website>' )
parser.add_argument('-a', '--alias', action='store', type=bool, nargs='?', const=True, default=False, help="Displays IP or Alias (CNAME)")
parser.add_argument('-c', '--count', action='store', type=int, default=-1, help="count")
parser.add_argument('-m', '--method', action='store', type=str, default="head", help="HTTP method [get or head]")
parser.add_argument('-o', '--output', action='store', type=str, default="text", help="Output [text|json]")
parser.add_argument('-q', '--quiet', action='store', type=bool, nargs='?', const=True, default=False, help="Reduced Verbosity")
parser.add_argument('-t', '--timeout', action='store', type=int, default=1, help="HTTP request timeout")
parser.add_argument('-w', '--wait', action='store', type=float, default=0, help="waittime")

args = parser.parse_args()

main( args.URL, args.alias , args.wait, args.quiet, args.output, args.method, args.timeout, args.count )