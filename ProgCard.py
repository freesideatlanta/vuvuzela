#!/usr/bin/python
#
#   ProgCard.py  1.0
#
#   Send command to program new cards into the Viking ES-1
#
#   2010.03.06 - K.C. Budd
#
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

######## logit(logline)
#
# 
def logit(logline):
   try:
      syslog.openlog("Viking ES-1",0,syslog.LOG_LOCAL1)
      syslog.syslog(logline)
      syslog.closelog()
   except:
      print "Unexpected error (syslog):", sys.exc_info()[0]
      raise
#
########


def usage():
   print "Usage: %s xxx yyyyy" % sys.argv[0]
   print ""
   print "Where:   xxx = ES-1 Slot ID"
   print "       yyyyy = Card Number"
   print ""
   exit()

########  main()...
#
def main():
   argc=len(sys.argv)
   if (argc != 3):
      usage()

   try:
      ser = serial.Serial(1,19200,timeout = 10)
   except:
      logit("Unexpected error (serial)")
      logit(str(sys.exc_info()[1]))
      raise

   logline = "ProgCard: Adding " + sys.argv[2] + " to slot " + sys.argv[1]
   logit(logline)
   es1_cmd = "ATX0DT " + sys.argv[2] + "#" + sys.argv[1] + ";H0\r"
   ser.write(es1_cmd);

   y = 0
   while(1):
      line=ser.readline()
      if line[:2] == 'OK':
         logit("ProgCard: Success")
         break
      else:
         y = y + 1
         if y > 3:
            logit("ProgCard: Failed.  Check modem.")
            ser.close()
            exit(255)
   ser.close()
   exit(0)
#
# 
########  end main()...

if __name__ == '__main__':
   main() 
