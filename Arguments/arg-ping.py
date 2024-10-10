#!/usr/bin/env python

import argparse
import os
from time import sleep

parser = argparse.ArgumentParser(description="Ping a Host")
parser.add_argument('Host', help = "Enter an IP or Host Name", type = str)
args= parser.parse_args()

while True:
    try:
        command = f' ping -c 1 {args.Host}'
        response = os.popen(command)
        response = response.read()
    except:
        response = "Fail"

    os.system('cls')
    print(command)
    print(response)
    sleep(1)