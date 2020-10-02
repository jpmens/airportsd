AIRPORTSD(8)							  AIRPORTSD(8)



NAME
       airportsd ‐ IATA airport code lookup server

SYNOPSIS
       airportsd [‐v]

DESCRIPTION
       airportsd  is  an IATA airport code lookup daemon thing, accessible via
       HTTP.  When running on a tty the program will  output  brief  debugging
       information.

       The (curently hardcoded) CDB database must exist and be readable by the
       owner of the airportsd process.

EXAMPLE
	      $ curl ‐i http://127.0.0.1:8812/lookup?iata=bcn
	      HTTP/1.1 200 OK
	      Connection: Keep‐Alive
	      Content‐Length: 87
	      Content‐Type: application/json
	      Date: Fri, 02 Oct 2020 09:49:30 GMT
	      {
		"iata": "BCN",
		"cc": "Spain",
		"city": "Barcelona",
		"lat": "41.2971",
		"lon": "2.07846",
		"name": "Barcelona International Airport"
	      }

ENDPOINTS
       All airportsd API endpoints are obtained via GET requests.

   lookup
       This endpoint expects iata query  parameter  with  a  case  insensitive
       3‐letter  IATA  airport	code; the key is looked up in the database and
       the JSON data or HTTP status code 404 are returned.

OPTIONS
       airportsd understands the following global options.

       ‐v     show version information and exit

ENVIRONMENT
       AIRPORTSD_IP
	      optionally sets the listen address for  airportsd;  defaults  to
	      127.0.0.1  and we strongly recommend this is not changed to any‐
	      thing other than a loopback address.

       AIRPORTSD_PORT
	      optionally sets the TCP listen port to something other than  the
	      default 8812.

REQUIREMENTS
   freebsd
	      $ pkg install libmicrohttpd
	      $ pkg install tinycdb

	      $ cat > config.mk <<EOF
	      LISTEN_HOST=   "127.0.0.1"
	      LISTEN_PORT=   "8812"
	      INC =	      ‐I/usr/local/include
	      LIBS =	      ‐L /usr/local/lib
	      EOF

   rhel/centos
	      yum install tinycdb

   debian
	      apt‐get install tinycdb

   macos
	      brew install libmicrohttpd tinycdb

   all
       · libmicrohttpd (https://www.gnu.org/software/libmicrohttpd/)

       · tinycdb (http://www.corpit.ru/mjt/tinycdb.html)

CREDITS
       · Airport   data,  downloaded  on  2020‐10‐01  (https://github.com/jpa‐
	 tokal/openflights/blob/master/data/airports.dat?raw=true), and origi‐
	 nally	 gratefully   provided	 by   openflights.org	(https://open‐
	 flights.org/data.html).

AVAILABILITY
       <https://github.com/jpmens/airportsd>

AUTHOR
       Jan‐Piet Mens <https://jpmens.net>



User Manuals							  AIRPORTSD(8)
