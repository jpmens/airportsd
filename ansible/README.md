# Ansible lookup plugin airport.py


```console
$ export ANSIBLE_LOOKUP_PLUGINS=/path/to/this/directory/
```

```
PLAY [localhost] ********************************************************************

TASK [debug] ************************************************************************
ok: [localhost] => {
    "msg": "FRA is Frankfurt am Main Airport in Frankfurt am Main"
}

TASK [debug] ************************************************************************
ok: [localhost] => {
    "msg": "Barcelona is at https://openstreetmap.org/?mlat=41.2971&mlon=2.07846&zoom=12"
}

TASK [debug] ************************************************************************
ok: [localhost] => {
    "fra": {
        "cc": "DE",
        "city": "Frankfurt am Main",
        "iata": "FRA",
        "lat": "50.033333",
        "lon": "8.570556",
        "name": "Frankfurt am Main Airport",
        "osm": "https://openstreetmap.org/?mlat=50.033333&mlon=8.570556&zoom=12"
    }
}
```
