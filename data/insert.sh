#!/bin/sh

USER=vuvuzela
PASS=alezuvuv
DB=freeside
TARGET=insert.sql

:> $TARGET
cat insert_person.sql >> $TARGET
cat insert_user.sql >> $TARGET
cat insert_group.sql >> $TARGET
cat insert_token.sql >> $TARGET
cat insert_zone.sql >> $TARGET

mysql -u $USER --password=$PASS $DB < $TARGET

rm $TARGET
