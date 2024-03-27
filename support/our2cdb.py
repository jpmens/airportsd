#!/usr/bin/env python3

# Copyright (C) 2020 Jan-Piet Mens <jp@mens.de>
# our2cdb.py: read airports.csv CSV and produce key_JSON for passing to cdb(1)

import csv
import json
import sys

sys.path.append("support/emoji-flags")
from emojiflags.lookup import lookup

with open('airports.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        (id, ident, atype, name, lat, lon, alt, continent, cc, region, city,
           scheduled, gps_code, iata, localcode, home, wikipedia, keywords) = row

        # atype == airport type

        if atype in [ 'closed', 'small_airport', 'medium_airport', 'large_airport' ]:
            if iata != "" and len(iata) == 3:
                data = {
                    "id"     : id,
                    "iata"   : iata,
                    "cc"     : cc,
                    "city"   : city,
                    "lat"    : lat,
                    "lon"    : lon,
                    "name"   : name,
                    "type"   : atype,
                    "emoji"  : lookup(cc),
                }
                print("{iata} {data}".format(iata=iata.upper(), data=json.dumps(data)))
        
