from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display
from ansible.module_utils.urls import open_url
from ansible.errors import AnsibleError, AnsibleOptionsError, AnsibleLookupError
import json

# Copyright (C) 2020-2024 Jan-Piet Mens <jp@mens.de>

DOCUMENTATION = """
    lookup: airport
    author: Jan-Piet Mens (@jpmens)
    version_added: "2.10"
    short_description: Queries IATA airports from airportsd
    description:
        - Queries the airportsd server for a case-insensitive, 3-letter
          IATA code and returns the JSON, enriched with an element "osm"
          containing a URL to OpenStreetMap at that location. Raises an
          AnsibleLookupError if the code cannot be queried.
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

display = Display()


class LookupModule(LookupBase):
    def __init__(self, *args, **kwargs):
        pass

    def run(self, terms, variables, **kwargs):
        ret = []
        for term in terms:
            display.debug("Airport lookup term: %s" % term)
            url = "http://127.0.0.1:8812/lookup?iata={0}".format(term)
            display.vvvv("Airport GET %s" % url)
            try:
                response = open_url(url)
            except Exception as e:
                raise AnsibleLookupError("The 'airport' lookup could not lookup IATA code '%s'" % term, orig_exc=e)


            data = json.loads(response.read())

            if 'lat' in data and 'lon' in data:
                data['osm'] = "https://openstreetmap.org/?mlat={0}&mlon={1}&zoom=12".format(data['lat'], data['lon'])

            ret.append(data)

        return ret
