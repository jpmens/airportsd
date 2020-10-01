# airportsd

## credits

- Airport data, downloaded on 2020-10-01 from [here](https://github.com/jpatokal/openflights/blob/master/data/airports.dat?raw=true), and originally gratefully provided by [openflights.org](https://openflights.org/data.html). I use the simple dat2cdb.py to convert the CSV into input for a CDB file keyed on uppercase 3-letter IATA code (e.g. BCN for Barcelona). The payload in the CDB is a JSON object:

/'";\|\]}
$ cdb -q airports.cdb BCN
{"iata": "BCN", "cc": "Spain", "city": "Barcelona", "lat": "41.2971", "lon": "2.07846"}



libicrohttp
cdb
