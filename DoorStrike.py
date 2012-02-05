#!/usr/bin/python
#
#   DoorStrike.py  1.0
#
#   Send command to momentarily strike the door to the Viking ES-1
#
#   2009.12.26 - K.C. Budd
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

########  main()...
#
def main():

   try:
      ser = serial.Serial(1,19200,timeout = 10)
   except:
      logit("Unexpected error (serial)")
      logit(str(sys.exc_info()[1]))
      raise

   ser.write("ATX0DT*6;H0\r");
   y = 0
   while(1):
      line=ser.readline()
      if line[:2] == 'OK':
         print "Success."
         break;
      else:
         y = y + 1
         if y > 3:
            print "Failed.  Check modem."
            ser.close()
            exit(255)
   ser.close()
   exit(0)

#         logline="["+str(serialno)+"] Door: " + a_door + " Card ID: " + a_card + " Result: " + a_result
#         logit(logline)
# 
########  end main()...

if __name__ == '__main__':
   main() 
