#!/usr/bin/python
# AccessHandler.py
#   Should be called for each access attempt
#   Usage:   AccessHandler.py ABCCCDDDDD
#
#   Where:   A = Door ID
#            B = Access Result (V,N,F as per ES-1 Documentation)
#            CCC = Facility Code
#            DDDDD = Card ID           
#

import string
import sys
import os
import re
import signal
import time
import MySQLdb
import twitter
import ConfigParser
import datetime,time
import syslog

######## usage()
#
def usage():
   print "Usage: "
   print "   %s ABCCCDDDDD" % sys.argv[0]
   print "   Where:   A = Door ID"
   print "            B = Access Result (V,N,F as per ES-1 Documentation)"
   print "            CCC = Facility Code"
   print "            DDDDD = Card ID"
   print ""
   sys.exit(1)
#
### End usage()


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


######## run(program[, arg (...)])
#
def run(program, *args):
    pid = os.fork()
    if not pid:
        os.execvp(program, (program,) +  args)
#    return os.wait()[0]
#
########


######## granted_sound(cardID)
#
def granted_sound(cardID):
    # NOTE: it's reading these characters and deciding to look up iButton user (?)
   if (cardID[:3] == "001"):
      conn = dbconnect()
      cursor = conn.cursor()
      cursor.execute("""
         SELECT id FROM members WHERE iButton = %s
         """,(cardID))
      try:
         memberID = "%03d" % cursor.fetchone()[0]
      except:  # Something went wrong!
        logit("AccessHandler: Error - granted iButton not in member DB!")
        memberID = None
   else:
      memberID = None

   SOUNDPATH="/home/DoorSounds/"

   s_exists = 0
   defaultsound = SOUNDPATH + "welcome.wav"

   # Check for MP3 file
   if (memberID):
      soundfile = SOUNDPATH + "member" + memberID + ".mp3"
   else:
      soundfile = SOUNDPATH + cardID + ".mp3"
   try:
      s_exists = os.stat(soundfile)
   except:
      pass

   if (not s_exists):
      # Check for WAV file
      if (memberID):
         soundfile = SOUNDPATH + "member" + memberID + ".wav"
      else:
         soundfile = SOUNDPATH + cardID + ".wav"
      try:
         s_exists = os.stat(soundfile)
      except:
         pass

   if (s_exists):
      run("/usr/bin/play","-q",soundfile,"trim","0","12")  # Play the first 12 seconds.
   else:
      run("/usr/bin/play","-q",defaultsound)  # Play the generic welcome sound
   
#
### end granted_sound()


###########
#
# dbconnect() : Connect to MySQL Database and return conn object
#
def dbconnect():
   dbhost="localhost"
   dbuser="logger"
   dbpw="SkyMotel"
   dbname="freesidemembers"
   try:
      conn = MySQLdb.connect(
         host = dbhost, user = dbuser,
         passwd = dbpw, db = dbname)
   except MySQLdb.Error, e:
      print logdate() + " Error %d: %s" % (e.args[0], e.args[1])
      sys.exit(1)
   return conn
#
## END dbconnect()

######## iB_enroll_arm(cardID)
#
# 1. if you use a cardID that doesn't have a freeside facilityID of 040, then find the user's corresponding iButtonID
# 2. if you haven't assigned an iButtonID to a user, then create a temporary file iBmarker with the user's "cardID" CCCDDDDD
# NOTE: this looks to be the first step in a process to register an iButton with a user
def iB_enroll_arm(cardID):
    # NOTE: this is not a cardID, this is CCCDDDDD
    # NOTE: this is what I think the facilityID at freeside is
    # NOTE: this examines the first three characters, so the facility code
   if (cardID[:3] != "040"):
      return
   conn = dbconnect()
   cursor = conn.cursor()
   cursor.execute("""
      SELECT iButton FROM members WHERE cardID = %s
      """,(cardID))
#   try:
   iButton = cursor.fetchone()[0]
#   except:  # Something went wrong!
#      LOG HERE
   if (iButton == None):   # Okay, there isn't one assigned yet
       # NOTE: iButton markers stored in this file - looks to be ibutton
      mrkfile = open("/var/tmp/iBmarker","w")
      mrkfile.write(str(time.mktime(datetime.datetime.now().timetuple()))+"|"+cardID)
      mrkfile.flush()
      mrkfile.close()
   return
#
######## done.      


######## iB_enroll(cardID)
#
# 1. look for iBmarker file
# 2. if iBmarker exists, this means that somebody used a cardID with a non 040 facilityID
# 2a. that probably means there's a special card to register iButtons, but it could be any readable card without a facilityID of 040
# 3. if either there's no iBmarker, or if you don't tap an iButton in 20 seconds, then it breaks out without registering
# 4. clear the iBmarker file
# 5. find the member ID (the 'primary' key of the members table) that corresponds to the user's cardID
# 6. NOTE: the es1_slot assigned to the iButton is 100 more than the member ID - could be problematic
# 7. the comment suggests that the old badge is not valid...maybe replaces a user's login with the ibutton?
# NOTE: there's little to no mention of the iButton in the original access handler
def iB_enroll(cardID):
   try:
      mrkfile = open("/var/tmp/iBmarker","r")
   except:
      logit("AccessHandler: iB_invalid: No recent badge activity.  Disregarding.")
      granted_sound("buzzer")
      return
   mrkr = mrkfile.readline()
   mstamp = float(mrkr[:mrkr.index("|")])
   mdelta = time.mktime(datetime.datetime.now().timetuple()) - mstamp
   if (mdelta > 20): 
      logit("AccessHandler: iB_invalid: No recent badge activity.  Disregarding.")
      granted_sound("buzzer")
      return
   mcardID = mrkr[mrkr.index("|")+1:]
   mrkfile.close()

   os.remove("/var/tmp/iBmarker")

   conn = dbconnect()
   cursor = conn.cursor()
   cursor.execute("""
      SELECT id FROM members WHERE cardID = %s
      """,(mcardID))
   mID = int(cursor.fetchone()[0])
   cursor.execute("""
      UPDATE members SET iButton = %s WHERE cardID = %s
      """,(cardID,mcardID))
   cursor.close
   es1_slot = mID + 100
   logline = "AccessHandler: Enroll " + cardID + " in slot " + str(es1_slot) + ".  Old card: " + mcardID
   logit(logline)
   granted_sound("enroll")
   run("/home/DoorLogger/ProgCard.py",str(es1_slot),cardID)
   logit("AccessHandler: Enrollment complete.")
   return
#
######## done.


######## tweet_alias(cardID)
#
def tweet_alias(cardID):
   conn = dbconnect()
   cursor = conn.cursor()
   cursor.execute("""
      SELECT alias FROM members WHERE cardID = %s OR iButton = %s
      """,(cardID,cardID))
   try:
      alias = cursor.fetchone()[0]
   except:  # User not in db!
      alias = "*UNKNOWN*"
   cursor.close()

   configdict = ConfigParser.ConfigParser()
   configdict.read('/usr/local/etc/Tweet.ini')
   twituser=configdict.get('twitter', 'twituser')
   twitpass=configdict.get('twitter', 'twitpass')

   tapi = twitter.Api(username=twituser,password=twitpass)
   update = "Granted: %s" % alias

   TwitRetry=0   # Sometimes Twitter needs more than one attempt.
   while (TwitRetry < 4):
      try:
         tapi.PostUpdate(update)
         TwitRetry = 4
      except:
         TwitRetry = TwitRetry + 1
         time.sleep(5)
#
### end tweet...


######## main()...
#
#
def main():
   argc=len(sys.argv)
   if (argc != 2):
      usage()

   signal.signal(signal.SIGCHLD, signal.SIG_IGN)  # We want our children
                                                  # to die quietly

   line=re.sub('[^A-Z0-9]+','', sys.argv[1])[:10]
   A_result = line[1]
   # NOTE: take everything but the first two characters, so pass CCCDDDDD
   A_cardID = line[2:]

   if ( (A_result == "V") | (A_result == "F") ):   # Access Granted
      granted_sound(A_cardID)  # Play sound if it exists
      tweet_alias(A_cardID)
      # NOTE: if the badge has access then start the two-step process of enrolling an iButton
      iB_enroll_arm(A_cardID)
   else:  # Access Denied
      if (A_cardID[:3] == "001"):
          # NOTE: assuming the iButton fails, attempt to enroll it
         iB_enroll(A_cardID)
      else:
         granted_sound("buzzer")

   exit(0)
#
########

if __name__ == '__main__':
    main()
