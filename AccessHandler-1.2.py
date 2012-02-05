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
from twitter import Twitter, TwitterError
from twitter import OAuth, read_token_file
import ConfigParser

CONSUMER_KEY='uS6hO2sV6tDKIOeVjhnFnQ'
CONSUMER_SECRET='MEYTOS97VvlHX7K1rwHPEqVpTSqZ71HtvoK4sVuYk'

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
   SOUNDPATH="/home/DoorSounds/"
   s_exists = 0

   # Check for MP3 file
   soundfile = SOUNDPATH + cardID + ".mp3"
   defaultsound = SOUNDPATH + "welcome.wav"
   try:
      s_exists = os.stat(soundfile)
   except:
      pass

   if (not s_exists):
      # Check for WAV file
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

######## tweet_alias(cardID)
#
def tweet_alias(cardID):
   conn = dbconnect()
   cursor = conn.cursor()
   cursor.execute("""
      SELECT alias FROM members WHERE cardID = %s
      """,(cardID))
   try:
      alias = cursor.fetchone()[0]
   except:  # User not in db!
      alias = "*UNKNOWN*"
   cursor.close()

   oauth_token,oauth_token_secret = read_token_file('/usr/local/etc/twitter.oauth')

   tapi = Twitter( auth=OAuth( oauth_token, oauth_token_secret, CONSUMER_KEY, CONSUMER_SECRET),
		   secure=1, api_version='1', domain='api.twitter.com' )
   update = "Granted: %s" % alias

   TwitRetry=0   # Sometimes Twitter needs more than one attempt.
   while (TwitRetry < 4):
      try:
         tapi.statuses.update(status=update)
         TwitRetry = 4
      except:
	 print 'Error updating tiwtter. Retrying....'
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
   A_cardID = line[2:]

   if ( (A_result == "V") | (A_result == "F") ):   # Access Granted
      granted_sound(A_cardID)  # Play sound if it exists
      tweet_alias(A_cardID)
   else:  # Access Denied
      granted_sound("buzzer")

   exit(0)
#
########

if __name__ == '__main__':
    main()
