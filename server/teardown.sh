#!/bin/sh

CONFIGURATION=configuration.ini
LOGIN=$(awk -F ":" '/login/ {print $2}' $CONFIGURATION)
GROUP=$(awk -F ":" '/group/ {print $2}' $CONFIGURATION)

delgroup $GROUP
deluser $LOGIN
