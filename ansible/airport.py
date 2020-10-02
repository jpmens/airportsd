from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase
from ansible.module_utils.urls import open_url
import json

# Copyright (C) 2020 Jan-Piet Mens <jp@mens.de>

DOCUMENTATION = """
    lookup: airport
    author: Jan-Piet Mens (@jpmens)
    version_added: "2.10"
    short_description: Queries IATA airports from airportsd
    description:
        - Queries the airportsd server for a case-insensitive, 3-letter
          IATA code and returns the JSON, enriched with an element "osm"
          containing a URL to OpenStreetMap at that location.
    options:
        _terms:
            description:
                - The IATA codes to query
            type: list
            elements: string
            required: True
"""

EXAMPLES = """
    - debug: msg="{{ lookup('airport','bcn') }}"
"""

RETURN = """
    _raw:
        description: JSON response from query
"""


class LookupModule(LookupBase):
    def __init__(self, *args, **kwargs):
        pass

    def run(self, terms, variables, **kwargs):
        ret = []
        for term in terms:
            url = "http://127.0.0.1:8812/lookup?iata={iata}".format(iata=term)
            try:
                response = open_url(url)
            except Exception as e:
                raise AnsibleError("Received HTTP error for %s : %s" % (term, e))

            data = json.loads(response.read())

            if 'lat' in data and 'lon' in data:
                data['osm'] = "https://openstreetmap.org/?mlat={lat}&mlon={lon}&zoom=12".format(lat=data['lat'], lon=data['lon'])

            ret.append(data)

        return ret
