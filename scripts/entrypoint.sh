#!/bin/bash


set -m

export REQUEST_DB_FILENAME=/data/requests.sqlite
export USER_DB_FILENAME=/data/users.sqlite

pdns_server --config-dir=/etc/pdns &
/usr/bin/mess-with-dns