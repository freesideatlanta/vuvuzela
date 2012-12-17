#!/bin/sh

USER=root
PASS=fsroot
DB=freeside

mysql -u $USER -p $PASS $DB < insert_person.sql
mysql -u $USER -p $PASS $DB < insert_user.sql
mysql -u $USER -p $PASS $DB < insert_group.sql
mysql -u $USER -p $PASS $DB < insert_token.sql
mysql -u $USER -p $PASS $DB < insert_zone.sql
