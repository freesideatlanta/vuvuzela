#!/bin/sh

CONFIGURATION=configuration.ini
ACLPATH=$(awk -F ":" '/aclpath/ {print $2}' $CONFIGURATION)
LOGPATH=$(awk -F ":" '/logpath/ {print $2}' $CONFIGURATION)
LOGIN=$(awk -F ":" '/login/ {print $2}' $CONFIGURATION)
GROUP=$(awk -F ":" '/group/ {print $2}' $CONFIGURATION)

adduser --disabled-password --ingroup $GROUP $LOGIN
mkdir -pv -m g+w $ACLPATH
mkdir -pv -m g+w $LOGPATH
mkdir -pv -m g+w ~/.vuvuzela
chown -v $LOGIN:$GROUP $ACLPATH
chown -v $LOGIN:$GROUP $LOGPATH
chown -v $LOGIN:$GROUP ~/.vuvuzela
cp -pv $CONFIGURATION ~/.vuvuzela/.
