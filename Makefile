
include config.mk

CFLAGS= -Wall -Werror $(INC)
LDFLAGS=-lmicrohttpd -lcdb $(LIBS)

INSTALLDIR = /usr/local

CFLAGS += -DLISTEN_HOST=\"$(LISTEN_HOST)\"
CFLAGS += -DLISTEN_PORT=\"$(LISTEN_PORT)\"

OBJS = 

all: airportsd

airportsd: airportsd.c $(OBJS) Makefile version.h config.mk
	$(CC) $(CFLAGS) -o airportsd airportsd.c $(OBJS) $(LDFLAGS)

airports.cdb: airports.dat
	./dat2cdb.py | cdb -c -m -p 0444 airports.cdb

clean:
	rm -f *.o

clobber: clean
	rm -f airportsd

install: airportsd airports.cdb
	[ -d $(DESTDIR)$(INSTALLDIR)/bin ] || ( mkdir -p $(DESTDIR)$(INSTALLDIR)/bin; chmod 755 $(DESTDIR)$(INSTALLDIR)/bin )
	[ -d $(DESTDIR)$(INSTALLDIR)/sbin ] || ( mkdir -p $(DESTDIR)$(INSTALLDIR)/sbin; chmod 755 $(DESTDIR)$(INSTALLDIR)/sbin )
	mkdir -p $(DESTDIR)/var/local/airports
	chmod 755 $(DESTDIR)/var/local/airports
	mkdir -p $(DESTDIR)$(INSTALLDIR)/share/man/man1 $(DESTDIR)$(INSTALLDIR)/share/man/man8
	chmod 755 $(DESTDIR)$(INSTALLDIR)/share/man/man1 $(DESTDIR)$(INSTALLDIR)/share/man/man8
	install -m 755 airportsd $(DESTDIR)$(INSTALLDIR)/sbin/airportsd

	install -m 644 revgeod.1 $(DESTDIR)$(INSTALLDIR)/share/man/man8/revgeod.1

docs: airportsd.8 README.md

airportsd.8: revgeod.pandoc Makefile
	pandoc -s -w man+simple_tables -o $@ $<

#README.md: revgeod.pandoc Makefile
#	pandoc -s -w markdown_github+simple_tables $<  > $@
##	pandoc -s -w markdown+simple_tables $< | sed -n -e '4,$$p' > $@

