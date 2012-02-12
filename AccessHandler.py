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

import ConfigParser
import sqlite3

from twitter import Twitter, TwitterError
from twitter import OAuth, read_token_file
from ServiceLogger import debug, info, warning, error

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
    # TODO: re-enable and test
    info('playing sound')
    # run("/usr/bin/play", "-q", path, "trim", "0", "12")     
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
    retry = 0   
    while (retry < 4):
        try:
            tapi.statuses.update(status=message)
            retry = 5
        except:
            warning('Problem updating twitter, retry attempt = ')

        retry = retry + 1
        time.sleep(5)

    if (retry == 4):
        error('Timed out updating twitter')

def has_access(flag):
    # TODO: test
    return (flag == "V") | (flag == "F")

def get_username(cardID):
    # TODO: test
    # vuvuzela.db should reside in /var/run/vuvuzela
    connection = sqlite3.connect('vuvuzela.db')

    cursor = connection.cursor()
    params = { 'cardID' : cardID }
    cursor.execute("select username from members where cardID = :cardID", params)
    username = cursor.fetchone()

    return username

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

    if ( has_access(flag) ):
        info('member has access')
        
        username = get_username(cardID)
        debug('username = %s', username)

        execute_granted_actions(username)
    else:
        info('member is denied access')
        execute_denied_actions() 

    exit(0)

if __name__ == '__main__':
    main()
