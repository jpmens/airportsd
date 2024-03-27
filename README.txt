AIRPORTSD(8)							  AIRPORTSD(8)

NAME
       airportsd - IATA airport code lookup server

SYNOPSIS
       airportsd [-v]

DESCRIPTION
       airportsd is an HTTP-accessible IATA airport code lookup daemon.  We
       created this as a service students can use on lab machines for
       developing an Ansible lookup plugin during trainings.

       When running on a tty the program will output brief debugging
       information on startup, and when it’s queried.

       The (currently hard-coded) CDB database must exist and be readable by
       the owner of the airportsd process.

EXAMPLE

	      $ curl -i http://127.0.0.1:8812/lookup?iata=bcn
	      HTTP/1.1 200 OK
	      Date: Wed, 26 Mar 2024 22:17:20 GMT
	      Connection: close
	      Content-Type: application/json
	      Content-Length: 216
	      {
		  "id": "4004",
		  "iata": "BCN",
		  "cc": "ES",
		  "city": "Barcelona",
		  "lat": "41.2971",
		  "lon": "2.07846",
		  "name": "Josep Tarradellas Barcelona-El Prat Airport",
		  "type": "large_airport",
		  "emoji": "🇪🇸"
	      }


ENDPOINTS
       All airportsd API endpoints are obtained via GET requests.

   lookup
       This endpoint expects iata query parameter with a case insensitive
       3-letter IATA airport code; the key is looked up in the database and
       the JSON data or HTTP status code 404 are returned.

OPTIONS
       airportsd understands the following global options.

       -v     show version information and exit

ENVIRONMENT
       AIRPORTSD_IP
	      optionally sets the listen address for airportsd; defaults to
	      127.0.0.1 and we strongly recommend this is not changed to
	      anything other than a loopback address.

       AIRPORTSD_PORT
	      optionally sets the TCP listen port to something other than the
	      default 8812.

FILES
       /usr/local/share/airports.cdb
	      the database file to query.

REQUIREMENTS
   freebsd

	      $ pkg install libmicrohttpd tinycdb

	      $ cat > config.mk <<EOF
	      DBNAME= "/usr/local/share/airports.cdb"
	      LISTEN_HOST=   "127.0.0.1"
	      LISTEN_PORT=   "8812"
	      INC =	      -I/usr/local/include
	      LIBS =	      -L /usr/local/lib
	      EOF


   rhel/centos

	      yum install tinycdb


   debian

	      apt-get install tinycdb


   macos

	      brew install libmicrohttpd tinycdb


   all
       • libmicrohttpd (https://www.gnu.org/software/libmicrohttpd/)

       • tinycdb (http://www.corpit.ru/mjt/tinycdb.html)

CREDITS
       • Airport data gratefully put into the Public Domain by ourairports.com
	 (https://ourairports.com/data/).

       • Country emoji flags from Emoji Flags (https://github.com/jonathan-
	 kosgei/emoji-flags)

AVAILABILITY
       <https://github.com/jpmens/airportsd>

AUTHOR
       Jan-Piet Mens <https://jpmens.net>

User Manuals							  AIRPORTSD(8)
