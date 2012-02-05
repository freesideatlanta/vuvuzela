#!/bin/sh
/usr/bin/ps awx | /usr/bin/grep DoorLoggerd.py | /usr/bin/grep -v grep >/dev/null 2>&1
if [ ! $? -eq 0 ]; then
   logger "DoorLoggerd not running.  Restarting."
   /home/DoorLogger/DoorLoggerd.py
fi
