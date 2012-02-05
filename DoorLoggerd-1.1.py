#!/usr/bin/python
#
#   DoorLogger.py  v1.1
#
#   Simple program to syslog lines coming in from serial port
#   for Viking ES-1 access
#
#   2009.08.06 - K.C. Budd
#
#   2009.08.10 - Daemonized
#
import serial
import datetime
import time
import syslog
import re
import sys
import os
import string
import signal

######## run(program[, arg (...)])
#
#
def run(program, *args):
    pid = os.fork()
    if not pid:
        os.execvp(program, (program,) +  args)
#    return os.wait()[0]
#
########


########  main()...
#
def main():
   signal.signal(signal.SIGCHLD, signal.SIG_IGN)   # We want our children
                                                   # to die quietly
   serialno = 1

   try:
      ser = serial.Serial(0,1200,timeout = 4)
   except:
      syslog.syslog("Unexpected error (serial)")
      syslog.syslog(str(sys.exc_info()[1]))
      raise


   while(1):
      line = ser.readline()
      if (len(line) > 2):
         line=re.sub('[^A-Z0-9]+','', line)[:10]
         a_door=line[0]
         if ( (line[1] == "V") | (line[1] == "F") ):
           a_result = "GRANTED"
         else:
           a_result = "DENIED"
         a_card=line[2:5]+":"+line[5:]
         logline="["+str(serialno)+"] Door: " + a_door + " Card ID: " + a_card + " Result: " + a_result
         serialno = serialno + 1
         if (serialno == 100):
            serialno = 1
         syslog.syslog(logline)
         run("/home/DoorLogger/AccessHandler.py",line)
# 
########  end main()...

if __name__ == '__main__':

   # First, acquire SYSLOG ability:
   try:
      syslog.openlog("Viking ES-1",0,syslog.LOG_LOCAL1)
      syslog.syslog("Viking ES-1 Logging Initalized")
   except:
      print "Unexpected error (syslog):", sys.exc_info()[0]
      raise

   # Now that we have syslog, we can daemonize.
   # do the UNIX double-fork magic, see Stevens' "Advanced 
   # Programming in the UNIX Environment" for details (ISBN 0201563177)
   try: 
       pid = os.fork() 
       if pid > 0:
           # exit first parent
           sys.exit(0) 
   except OSError, e: 
       print >>sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror) 
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
      print >>sys.stderr, "fork #2 failed: %d (%s)" % (e.errno, e.strerror) 
      sys.exit(1) 

   # Redirect standard file descriptors, we can't use 'em anymore.
   sys.stdin = open('/dev/null', 'r')
   sys.stdout = open('/dev/null', 'w')
   sys.stderr = open('/dev/null', 'w')

   # Finally, start the daemon main loop
   main() 
