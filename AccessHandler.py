#!/usr/bin/env python

#   Should be called for each access attempt
#   Usage:   AccessHandler.py ABCCCDDDDD
#
#   Where:   A = Door ID
#            B = Access Result (V,N,F as per ES-1 Documentation)
#            CCC = Facility Code
#            DDDDD = Card ID           

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

# TODO: move the key and secret to a configuration file in /etc/vuvuzela
CONSUMER_KEY='uS6hO2sV6tDKIOeVjhnFnQ'
CONSUMER_SECRET='MEYTOS97VvlHX7K1rwHPEqVpTSqZ71HtvoK4sVuYk'

def usage():
    print "Usage: "
    print "   %s ABCCCDDDDD" % sys.argv[0]
    print "   Where:   A = Door ID"
    print "            B = Access Result (V,N,F as per ES-1 Documentation)"
    print "            CCC = Facility Code"
    print "            DDDDD = Card ID"
    print ""
    sys.exit(1)

def run(program, *args):
    pid = os.fork()
    if not pid:
        os.execvp(program, (program,) +  args)
#    return os.wait()[0]

def play_greeting(soundfile):


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
        # Play the first 12 seconds.
        run("/usr/bin/play", "-q", soundfile, "trim", "0", "12")     
    else:
        run("/usr/bin/play", "-q", defaultsound)  # Play the generic welcome sound

def dbconnect():
    # TODO: remove this function; no longer going to use mysql login/password, only sqlite
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

def tweet_alias(cardID):
    # TODO: we can obtain the desired user alias from the previous sqlite query, passed in here
    conn = dbconnect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT alias FROM members WHERE cardID = %s
        """, (cardID))

    try:
        alias = cursor.fetchone()[0]
    except:  
        # User not in db!
        alias = "*UNKNOWN*"

    cursor.close()

    # TODO: make sure we have a copy of the twitter.oauth file, or re-fetch from the twitter account
    oauth_token, oauth_token_secret = read_token_file('/usr/local/etc/twitter.oauth')
    tapi = Twitter( auth=OAuth( oauth_token, oauth_token_secret, CONSUMER_KEY, CONSUMER_SECRET), secure=1, api_version='1', domain='api.twitter.com' )
    # TODO: use a substitution string found in the user's .vuvuzela/config, or a default defined here
    update = "Granted: %s" % alias

    # Sometimes Twitter needs more than one attempt.
    TwitRetry = 0   
    while (TwitRetry < 4):
        try:
            tapi.statuses.update(status=update)
            TwitRetry = 4
        except:
	        print 'Error updating twitter. Retrying...'

        TwitRetry = TwitRetry + 1
        time.sleep(5)

def main():
    argc=len(sys.argv)
    if (argc != 2):
        usage()

    # We want our children to die quietly
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)  

    line=re.sub('[^A-Z0-9]+','', sys.argv[1])[:10]
    A_result = line[1]
    A_cardID = line[2:]

    if ( (A_result == "V") | (A_result == "F") ):
        # Access Granted
        
        # Play sound if it exists
        granted_sound(A_cardID)  
        tweet_alias(A_cardID)
    else:
        # Access Denied
        granted_sound("buzzer")

    exit(0)

if __name__ == '__main__':
    main()
