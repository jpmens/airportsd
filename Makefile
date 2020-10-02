
include config.mk

CFLAGS= -Wall -Werror $(INC)
LDFLAGS=-lmicrohttpd -lcdb $(LIBS)

INSTALLDIR = /usr/local

CFLAGS += -DDBNAME=\"$(DBNAME)\"
CFLAGS += -DLISTEN_HOST=\"$(LISTEN_HOST)\"
CFLAGS += -DLISTEN_PORT=\"$(LISTEN_PORT)\"

all: airportsd docs

airportsd: airportsd.c Makefile version.h config.mk
	$(CC) $(CFLAGS) -o airportsd airportsd.c $(LDFLAGS)

# Use dat2cdb.py to convert the CSV into input for a CDB file keyed on
# uppercase 3-letter IATA code (e.g. BCN for Barcelona). The payload
# in the CDB is a JSON object

airports.cdb: airports.dat
	./dat2cdb.py | cdb -c -m -p 0444 airports.cdb

clean:
	rm -f *.o

clobber: clean
	rm -f airportsd

install: airportsd airports.cdb
	[ -d $(DESTDIR)$(INSTALLDIR)/sbin ] || ( mkdir -p $(DESTDIR)$(INSTALLDIR)/sbin; chmod 755 $(DESTDIR)$(INSTALLDIR)/sbin )
	install -m 755 airportsd $(DESTDIR)$(INSTALLDIR)/sbin/airportsd

	mkdir -p $$(dirname $(DBNAME) )
	chmod 755 $$(dirname $(DBNAME) )
	install -m 444 airports.cdb $(DBNAME)

	mkdir -p $(DESTDIR)$(INSTALLDIR)/share/man/man8
	chmod 755 $(DESTDIR)$(INSTALLDIR)/share/man/man8
	install -m 644 airportsd.8 $(DESTDIR)$(INSTALLDIR)/share/man/man8/airportsd.8

docs: airportsd.8 README.md

airportsd.8: airportsd.pandoc Makefile
	pandoc -s -f markdown -o $@ $<

