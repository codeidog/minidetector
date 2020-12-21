#! /usr/bin/env bash
#set -e
#DB_NAME='minidetector'

createuser --superuser $DB_USER
createdb --owner $DB_USER $DB_NAME
psql -c "alter user $DB_USER with encrypted password '$DB_PWD';"
echo DONE!