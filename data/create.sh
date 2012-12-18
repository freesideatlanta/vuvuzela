#!/bin/sh

USER=vuvuzela
PASS=alezuvuv
DB=freeside
TARGET=create.sql

echo "CREATE DATABASE IF NOT EXISTS $DB" > create_$DB.sql
mysql -u $USER --password=$PASS < create_$DB.sql

:> $TARGET
cat create_person.sql >> $TARGET
cat create_user.sql >> $TARGET
cat create_class.sql >> $TARGET
cat create_token.sql >> $TARGET
cat create_zone.sql >> $TARGET
cat create_node.sql >> $TARGET
cat create_relay.sql >> $TARGET
cat create_log.sql >> $TARGET

cat create_user_class.sql >> $TARGET
cat create_user_token.sql >> $TARGET
cat create_class_node.sql >> $TARGET
cat create_node_relay.sql >> $TARGET

mysql -u $USER --password=$PASS $DB < create.sql

rm create.sql
