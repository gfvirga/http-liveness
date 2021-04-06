# http-liveness
Probe your web app and get its statistics

It looks like `ping` on purpose!

## Objective
I created this tool to quickily test the uptime of my deployments. This is a great tool to be used while testing downtime for DR failovers, pod rollouts, HA system upgrade, Load Balancers and more.

## TL;DR

```shell
% docker run -it --rm gfvirga/httpliveness https://www.google.com -c 4
Check https://www.google.com (['172.217.12.206']) response: 200
Check https://www.google.com (['172.217.12.206']) response: 200
Check https://www.google.com (['172.217.12.206']) response: 200
Check https://www.google.com (['172.217.12.206']) response: 200

 --- https://www.google.com HTTP requests statistics ---
4 HTTP requested, 4 200 responses
```

## Help

```shell
$ python3 ./httpliveness.py -h
usage: httpliveness.py [-h] [-a [ALIAS]] [-c COUNT] [-m METHOD] [-o OUTPUT] [-q [QUIET]] [-t TIMEOUT] [-w WAIT] host

Process some integers.

positional arguments:
  host                  Enter URL with the patter - http(s)://<website>

optional arguments:
  -h, --help            show this help message and exit
  -a [ALIAS], --alias [ALIAS]
                        Displays Alias (CNAME), instead of IP
  -c COUNT, --count COUNT
                        count
  -m METHOD, --method METHOD
                        HTTP method [get or head]
  -o OUTPUT, --output OUTPUT
                        Output [text|json]
  -q [QUIET], --quiet [QUIET]
                        Reduced Verbosity
  -t TIMEOUT, --timeout TIMEOUT
                        HTTP request timeout
  -w WAIT, --wait WAIT  waittime
```

## Examples

```shell
$ python3 ./httpliveness.py https://www.example.com -c 4     
Check https://www.example.com (['93.184.216.34']) response: 200
Check https://www.example.com (['93.184.216.34']) response: 200
Check https://www.example.com (['93.184.216.34']) response: 200
Check https://www.example.com (['93.184.216.34']) response: 200

 --- https://www.example.com HTTP requests statistics ---
4 HTTP requested, 4 200 responses
```

## Example with Alias (CNAME)

```shell
$ python3 ./httpliveness.py https://mail.google.com --alias --count 4 --method get
Check https://mail.google.com (googlemail.l.google.com) response: 200
Check https://mail.google.com (googlemail.l.google.com) response: 200
Check https://mail.google.com (googlemail.l.google.com) response: 200
Check https://mail.google.com (googlemail.l.google.com) response: 200

 --- https://mail.google.com HTTP requests statistics ---
4 HTTP requested, 4 200 responses
```
