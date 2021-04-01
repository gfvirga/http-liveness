FROM python
COPY . .
RUN pip3 install requests argparse
ENTRYPOINT ["python3", "/httpliveness.py" ]