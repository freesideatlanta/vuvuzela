#!/bin/sh

USER=vuvuzela
PASS=alezuvuv
DB=freeside

echo "DROP DATABASE IF EXISTS $DB" > drop_$DB.sql
mysql -u $USER --password=$PASS < drop_$DB.sql

