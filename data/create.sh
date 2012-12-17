#!/bin/sh

USER=root
PASS=fsroot
DB=freeside

echo "CREATE DATABASE IF NOT EXISTS $DB" > create_$DB.sql
mysql -u $USER -p $PASS < create_$DB.sql

mysql -u $USER -p $PASS $DB < create_person.sql
mysql -u $USER -p $PASS $DB < create_user.sql
mysql -u $USER -p $PASS $DB < create_group.sql
mysql -u $USER -p $PASS $DB < create_token.sql
mysql -u $USER -p $PASS $DB < create_zone.sql
mysql -u $USER -p $PASS $DB < create_node.sql
mysql -u $USER -p $PASS $DB < create_relay.sql
mysql -u $USER -p $PASS $DB < create_log.sql

mysql -u $USER -p $PASS $DB < create_user_group.sql
mysql -u $USER -p $PASS $DB < create_user_token.sql
mysql -u $USER -p $PASS $DB < create_group_node.sql
mysql -u $USER -p $PASS $DB < create_node_relay.sql

