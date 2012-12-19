#!/bin/sh

USER=vuvuzela
PASS=alezuvuv
DB=freeside
TARGET=insert.sql

:> $TARGET
cat insert_person.sql >> $TARGET
cat insert_user.sql >> $TARGET
cat insert_class.sql >> $TARGET
cat insert_token.sql >> $TARGET
cat insert_zone.sql >> $TARGET
cat insert_node.sql >> $TARGET
cat insert_relay.sql >> $TARGET

cat insert_user_token.sql >> $TARGET
cat insert_user_class.sql >> $TARGET
cat insert_class_node.sql >> $TARGET
cat insert_node_relay.sql >> $TARGET

mysql -u $USER --password=$PASS $DB < $TARGET

rm $TARGET
