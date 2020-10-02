/*
 * airportsd.c
 * Copyright (C) 2020 Jan-Piet Mens <jp@mens.de>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 */

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>
#include <signal.h>
#include <errno.h>
#include <time.h>
#include <ctype.h>
#include <getopt.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/select.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <cdb.h>
#define MHD_PLATFORM_H
#include <microhttpd.h>
#include "version.h"

struct MHD_Daemon *mhdaemon;
struct cdb cdb;

static void catcher(int sig)
{
	if (sig == SIGINT) {
		MHD_stop_daemon(mhdaemon);
		exit(1);
	}
}

static void ignore_sigpipe()
{
	struct sigaction oldsig;
	struct sigaction sig;

	sig.sa_handler = &catcher;
	sigemptyset(&sig.sa_mask);
#ifdef SA_INTERRUPT
	sig.sa_flags = SA_INTERRUPT;	/* SunOS */
#else
	sig.sa_flags = SA_RESTART;
#endif
	if (0 != sigaction(SIGPIPE, &sig, &oldsig))
		fprintf(stderr,
		"Failed to install SIGPIPE handler: %s\n", strerror(errno));
}

static int send_content(struct MHD_Connection *conn, const char *page,
		const char *content_type, int status_code)
{
	int ret;
	struct MHD_Response *response;
	response = MHD_create_response_from_buffer(strlen(page),
				(void*) page, MHD_RESPMEM_MUST_COPY);
	if (!response)
		return (MHD_NO);
	MHD_add_response_header(response, "Content-Type", content_type);
	ret = MHD_queue_response(conn, status_code, response);
	MHD_destroy_response(response);
	return (ret);
}

static int send_page(struct MHD_Connection *conn, const char *page, int status_code)
{
	return send_content(conn, page, "text/plain", status_code);
}

static int get_lookup(struct MHD_Connection *connection)
{
	const char *iata;
	char *key, *kp, data[8192];
	unsigned keylen = 0, datalen;

	iata = MHD_lookup_connection_value(connection, MHD_GET_ARGUMENT_KIND, "iata");
	if (!iata || !*iata) {
		return send_page(connection, "Missing iata", 422);
	}

	if (!(key = strdup(iata))) {
		return send_page(connection, "out of memory", 422);
	}

	for (kp = key; kp && *kp; keylen++, kp++) {
		*kp = ( islower(*kp) ? toupper(*kp) : *kp );
	}

	fprintf(stderr, "Lookup: [%s]\n", key);

	if (cdb_find(&cdb, key, keylen) > 0) {
		datalen = cdb_datalen(&cdb);
		datalen = (datalen >= sizeof(data)) ? sizeof(data) : datalen;	/* cap */
		cdb_read(&cdb, data, datalen, cdb_datapos(&cdb));
		data[datalen] = 0;

		return send_content(connection, data, "application/json", MHD_HTTP_OK);
	}
	return send_page(connection, "not found", 404);
}

int handle_connection(void *cls, struct MHD_Connection *connection,
	const char *url, const char *method, const char *version,
	const char *upload_data, size_t *upload_data_size, void **con_cls)
{
	if (strcmp(method, "GET") != 0) {
		return (send_page(connection, "not allowed", MHD_HTTP_METHOD_NOT_ALLOWED));
	}

	if (strcmp(url, "/lookup") == 0) {
		return get_lookup(connection);
	}

	return send_page(connection, "four-oh-four", MHD_HTTP_NOT_FOUND);
}

int main(int argc, char **argv)
{
	struct sockaddr_in sad;
	char *s_ip, *s_port;
	unsigned short port;
	int ch, fd;

	if ((s_ip = getenv("AIRPORTSD_IP")) == NULL)
		s_ip = LISTEN_HOST;
	if ((s_port = getenv("AIRPORTSD_PORT")) == NULL)
		s_port = LISTEN_PORT;
	port = atoi(s_port);

	while ((ch = getopt(argc, argv, "v")) != EOF) {
		switch (ch) {
			case 'v':
				printf("airportsd %s\n", VERSION);
				exit(0);
			default:
				fprintf(stderr, "Usage: %s [-v]\n", *argv);
				exit(2);
		}
	}

	argc -= optind;
	argv += optind;


	memset(&sad, 0, sizeof (struct sockaddr_in));
	sad.sin_family = AF_INET;
	sad.sin_port = htons(port);
	if (inet_pton(AF_INET, s_ip, &(sad.sin_addr.s_addr)) != 1) {
		perror("Can't parse IP");
		exit(2);
	}


	if ((fd = open(DBNAME, O_RDONLY)) == -1) {
		perror(DBNAME);
		exit(3);
	}
	cdb_init(&cdb, fd);

	ignore_sigpipe();
	signal(SIGINT, catcher);

	mhdaemon = MHD_start_daemon(MHD_USE_SELECT_INTERNALLY, 0, NULL, NULL,
		&handle_connection, NULL,
		MHD_OPTION_SOCK_ADDR, &sad,
		MHD_OPTION_END);

	if (mhdaemon == NULL) {
		perror("Cannot initialize HTTP daemon");
		return (1);
	}

	while (1) {
		sleep(60);
	}

	MHD_stop_daemon(mhdaemon);
	cdb_free(&cdb);
	close(fd);
	return (0);
}
