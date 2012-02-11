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

def get_granted_sound(username):
    # TODO: implement
    #
    # path = "vuvuzela:default_granted_sound" from /var/run/vuvuzela/config.ini
    # detect ~<username>/.vuvuzela/config
    #
    # if exists
    #     path = "greeting" field value in config file // use os.stat(filename)
    #     
    # return path
    return ""

def get_denied_sound():
    # TODO: implement
    #
    # path = "vuvuzela:default_denied_sound" from /var/run/vuvuzela/config.ini
    # return path
    return ""

def play_sound(path):
    # TODO: test
    run("/usr/bin/play", "-q", path, "trim", "0", "12")     
    return

def get_message(username):
    # TODO: implement
    #
    # message = default message // "<username> has entered the building"
    # detect ~<username>/.vuvuzela/config
    #
    # if exists
    #     alias = "alias" field value in config file
    #     message = "message" field value in config file
    #
    #     if alias exists
    #         // modify the message, which presumably contains one %s
    #         message = "message", alias
    #
    # return message
    return ""

def tweet_message(message):
    # TODO: move the key and secret to a configuration file /var/run/vuvuzela/config.ini
    CONSUMER_KEY='uS6hO2sV6tDKIOeVjhnFnQ'
    CONSUMER_SECRET='MEYTOS97VvlHX7K1rwHPEqVpTSqZ71HtvoK4sVuYk'

    # TODO: make sure we have a copy of the twitter.oauth file, or re-fetch from the twitter account
    oauth_token, oauth_token_secret = read_token_file('/usr/local/etc/twitter.oauth')
    tapi = Twitter( auth=OAuth( oauth_token, oauth_token_secret, CONSUMER_KEY, CONSUMER_SECRET), secure=1, api_version='1', domain='api.twitter.com' )

    # Sometimes Twitter needs more than one attempt.
    TwitRetry = 0   
    while (TwitRetry < 4):
        try:
            tapi.statuses.update(status=message)
            TwitRetry = 4
        except:
	        print 'Error updating twitter. Retrying...'

        TwitRetry = TwitRetry + 1
        time.sleep(5)

def has_access(flag):
    # TODO: test
    return (flag == "V") | (flag == "F")

def get_username(cardID):
    # TODO: implement
    #
    # make a connection to the /var/run/vuvuzela/vuvuzela.db sqlite file
    # select from the members table the username for the cardID
    # return username
    return ""

def execute_granted_actions(username):
    # TODO: test 
    soundpath = get_granted_sound(username)
    message = get_message(username)

    play_sound(soundpath)
    tweet_message(message)

def execute_denied_actions():
    # TODO: test
    soundpath = get_denied_sound()

    play_sound(soundpath)

def main():
    argc = len(sys.argv)
    if (argc != 2):
        usage()

    # We want our children to die quietly
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)  

    line = re.sub('[^A-Z0-9]+','', sys.argv[1])[:10]
    flag = line[1]
    cardID = line[2:]

    if ( has_access(flag) )
        username = get_username(cardID)
        execute_granted_actions(username)
    else:
        execute_denied_actions() 

    # TODO: remove this section
    if ( (flag == "V") | (cardID == "F") ):
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
