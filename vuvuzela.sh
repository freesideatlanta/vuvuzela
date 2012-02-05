#!/bin/sh
/usr/bin/ps awx | /usr/bin/grep vuvuzelad | /usr/bin/grep -v grep >/dev/null 2>&1
if [ ! $? -eq 0 ]; then
   logger "vuvuzelad not running.  Restarting."
   /home/vuvuzela/bin/vuvuzelad.py
fi
