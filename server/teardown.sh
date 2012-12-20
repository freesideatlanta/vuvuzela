#!/bin/sh

CONFIGURATION=configuration.ini
LOGIN=$(awk -F ":" '/login/ {print $2}' $CONFIGURATION)
GROUP=$(awk -F ":" '/group/ {print $2}' $CONFIGURATION)

deluser --remove-all-files $LOGIN $GROUP
