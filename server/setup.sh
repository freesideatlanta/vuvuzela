#!/bin/sh

# use sudo to run this script

CONFIGURATION=configuration.ini
ACLPATH=$(awk -F ":" '/aclpath/ {print $2}' $CONFIGURATION)
LOGPATH=$(awk -F ":" '/logpath/ {print $2}' $CONFIGURATION)
LOGIN=$(awk -F ":" '/login/ {print $2}' $CONFIGURATION)
GROUP=$(awk -F ":" '/group/ {print $2}' $CONFIGURATION)

addgroup $GROUP
adduser --disabled-password --ingroup $GROUP $LOGIN
mkdir -pv -m g+w $ACLPATH
mkdir -pv -m g+w $LOGPATH
mkdir -pv -m g+w /home/vuvuzela/.vuvuzela
cp -pv $CONFIGURATION /home/vuvuzela/.vuvuzela/.
chown -vR $LOGIN:$GROUP /home/vuvuzela/.vuvuzela
chown -vR $LOGIN:$GROUP $ACLPATH
chown -vR $LOGIN:$GROUP $LOGPATH
