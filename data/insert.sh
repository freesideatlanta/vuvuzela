#!/bin/sh

USER=root
PASS=fsroot
DB=freeside
TARGET=insert.sql

:> $TARGET
cat insert_person.sql >> $TARGET
cat insert_user.sql >> $TARGET
cat insert_group.sql >> $TARGET
cat insert_token.sql >> $TARGET

mysql -u $USER -p $PASS $DB < $TARGET
