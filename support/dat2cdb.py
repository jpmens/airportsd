#!/usr/bin/env python3

# Copyright (C) 2020 Jan-Piet Mens <jp@mens.de>
# dat2cdb.py: read airports.dat CSV and produce key_JSON for passing to cdb(1)

import csv
import json

with open('airports.dat', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        (id, name, city, country, iata, icao, lat, lon, alt, tz, dst, tzdb, typ, source) = row
        if iata != "\\N":
            data = {
                "iata"   : iata,
                "cc"     : country,
                "city"   : city,
                "lat"    : lat,
                "lon"    : lon,
                "name"   : name,
            }
            print("{iata} {data}".format(iata=iata.upper(), data=json.dumps(data)))
        
