#!/usr/bin/env python3

# Copyright (C) 2020-2024 Jan-Piet Mens <jp@mens.de>
# q.py: simple query utility for airportd

import sys
import requests
import json

url = "http://127.0.0.1:8812/lookup?iata={iata}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {p} IATA".format(p=sys.argv[0]))
        exit(2)

    r = requests.get(url.format(iata=sys.argv[1]))
    if r.status_code == 200:
        print(json.dumps(r.json(), indent=4))
    else:
        print(r.status_code)
