#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JP Mens -- create nairports.py for use in Ansible exercise

import csv
import json
import sys
import datetime

arr = []

with open('../../airports.csv', newline='', encoding='utf-8') as csvfile:
    airreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    n = 0
    for row in airreader:
        # if "iata_code" in row and len(row["iata_code"]) > 0:
        if row["type"] == "large_airport" and "Spam".lower() not in row["name"].lower():
            data = {
                "cc"    : row["iso_country"],
                "lat"   : row["latitude_deg"],
                "lon"   : row["longitude_deg"],
                "iata"  : row["iata_code"],
                "name"  : row["name"],
            }
            arr.append(data)

print("""#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import random
""")
print("# assembled by mk-nairports.py on {0}\n".format(datetime.date.today().isoformat()))

print("airports =", json.dumps(arr, indent=1))

print("""

payload = random.choice(airports)
print(json.dumps(payload, indent=4))

""")
