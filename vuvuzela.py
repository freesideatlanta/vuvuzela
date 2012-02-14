#!/usr/bin/env python
# this is the vuvuzela "service" that listens for badge read events, and calls AccessHandler.py
# NOTE: this script does some amusing double-fork action to detatch its process from the parent
# NOTE: the upstart configuration notes this and asserts the vuvuzela service double-folks

import datetime
import os
import re
import serial
import signal
import string
import sys
import syslog
import time

import sqlite3

from ServiceLogger import debug, info, warning, error

def run(program, *args):
    pid = os.fork()
    if not pid:
        os.execvp(program, (program,) +  args)
#    return os.wait()[0]

def logit(logline):
    try:
        syslog.openlog("Viking ES-1", 0, syslog.LOG_LOCAL1)
        syslog.syslog(logline)
        syslog.closelog()
    except:
        error("Unexpected error (syslog): %s", sys.exc_info()[0])
        raise

def main():
    # We want our children to die quietly
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)   
    serialno = 1

    while(1):
        try:
            ser = serial.Serial('/dev/ttyS0', 1200, timeout = 60)
        except:
            logit("Unexpected error (serial)")
            logit(str(sys.exc_info()[1]))
            raise

        line = ser.readline()
        ser.close()
        if (len(line) > 2):
            line = re.sub('[^A-Z0-9]+', '', line)[:10]
            a_door = line[0]

            if ( (line[1] == "V") | (line[1] == "F") ):
                a_result = "GRANTED"
            else:
                a_result = "DENIED"
         
        a_card=line[2:5]+":"+line[5:]
        logline = "[" + str(serialno) + "] Door: " + a_door + " Card ID: " + a_card + " Result: " + a_result
        serialno = serialno + 1
         
        if (serialno == 100):
            serialno = 1
         
        logit(logline)
        # TODO: determine if the access handler (or other python files) need to reside in /var/run/vuvuzela
        run("AccessHandler.py", line)

if __name__ == '__main__':
    logit("Viking ES-1 Logging Initalized")

    # do the UNIX double-fork magic, see Stevens' "Advanced 
    # Programming in the UNIX Environment" for details (ISBN 0201563177)
    try: 
        pid = os.fork() 
        if pid > 0:
            # exit first parent
            sys.exit(0) 
    except OSError, e: 
        print >> sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror) 
        sys.exit(1)

    # decouple from parent environment
    os.chdir("/") 
    os.setsid() 
    os.umask(0) 

    # do second fork
    try: 
        pid = os.fork() 
        if pid > 0:
            # exit from second parent, print eventual PID before
            print "Daemon PID %d" % pid 
            sys.exit(0) 
    except OSError, e: 
        print >> sys.stderr, "fork #2 failed: %d (%s)" % (e.errno, e.strerror) 
        sys.exit(1) 

    # Redirect standard file descriptors, we can't use 'em anymore.
    sys.stdin = open('/dev/null', 'r')
    sys.stdout = open('/dev/null', 'w')
    sys.stderr = open('/dev/null', 'w')

    # Finally, start the daemon main loop
    main() 
