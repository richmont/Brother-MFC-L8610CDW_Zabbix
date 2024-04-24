#!/usr/bin/python
# Author: Richelmy Monteiro
# Date: april/2024
# version 1.0
# License: GPL 3.0
import sys
import requests
from bs4 import BeautifulSoup
try:
    # get the IP from printer from first parameter
    url = sys.argv[1]
    # and the supply in the second
    supply = sys.argv[2]

    data = requests.get(f"http://{url}/general/status.html", timeout=3).text
    soup = BeautifulSoup(data, 'html.parser')

    list_toner_remain = soup.select("img.tonerremain")

    status_list = soup.select("span.moni")
    tag_black = list_toner_remain[0]
    tag_cyan = list_toner_remain[1]
    tag_magenta = list_toner_remain[2]
    tag_yellow = list_toner_remain[3]

    black_supply_level = int(tag_black['height'])
    cyan_supply_level = int(tag_cyan['height'])
    magenta_supply_level = int(tag_magenta['height'])
    yellow_supply_level = int(tag_yellow['height'])

    if supply=="black":
        # print to output the value and return sucess to SO
        print(black_supply_level)
        sys.exit(0)
    if supply=="cyan":
        print(cyan_supply_level)
        sys.exit(0)
    if supply=="magenta":
        print(magenta_supply_level)
        sys.exit(0)
    if supply=="yellow":
        print(yellow_supply_level)
        sys.exit(0)
    if supply=="status":
        print(status_list[0].text)
        sys.exit(0)
    else:
        print("Check the supply requested, available options:")
        print("black, yellow, magenta, cyan and status")
        sys.exit(2)
except IndexError as e:
    # show usage when parameters is not present and return error to SO
    print("Usage: script.py <printer_ip_address> <supply_type>")
    sys.exit(2)
except requests.exceptions.ConnectionError:
    print("Connection error with printer, check IP address and try again")
    sys.exit(2)