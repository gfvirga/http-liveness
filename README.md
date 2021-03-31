# http-liveness
Probe your web app and get its statistics

# Help

```shell
% python3 ./httpliveness.py -h                      
usage: httpliveness.py [-h] [-a [ALIAS]] https://www.example.com

Process some integers.

positional arguments:
  https://www.example.com

optional arguments:
  -h, --help            show this help message and exit
  -a [ALIAS], --alias [ALIAS]
                        Returns IP or Alias
```

# Example

```shell
% python3 ./httpliveness.py https://google.com        
Check https://google.com (['172.217.10.142']) response: 200
Check https://google.com (['172.217.10.142']) response: 200
Check https://google.com (['172.217.10.142']) response: 200
Check https://google.com (['172.217.10.142']) response: 200
^C
 --- https://google.com HTTP requests statistics ---
5 HTTP requested, 4 200 responses
```

# Example with Alias (CNAME)

```shell
gfvirga@Gabriels-MacBook-Pro http-liveness % python3 ./httpliveness.py https://mail.google.com --alias
Check https://mail.google.com (googlemail.l.google.com) response: 200
Check https://mail.google.com (googlemail.l.google.com) response: 200
Check https://mail.google.com (googlemail.l.google.com) response: 200
Check https://mail.google.com (googlemail.l.google.com) response: 200
Check https://mail.google.com (googlemail.l.google.com) response: 200
^C
 --- https://mail.google.com HTTP requests statistics ---
6 HTTP requested, 5 200 responses
```