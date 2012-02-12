#!/usr/bin/env python

#   Should be called for each access attempt
#   Usage:   AccessHandler.py ABCCCDDDDD
#
#   Where:   A = Door ID
#            B = Access Result (V,N,F as per ES-1 Documentation)
#            CCC = Facility Code
#            DDDDD = Card ID           

import datetime
import os
import re
import signal
import string
import sys
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

def get_granted_sound(parser):
    # TODO: test
    # make sure this is /var/run/vuvuzela/config.ini
    parser.read('config.ini')
    path = parser.get('sound', 'granted')

    configpath = os.path.expanduser('~/.vuvuzela/config.ini')
    if (os.access(configpath, os.R_OK)):
        parser.read(configpath)
        if (parser.has_option('sound', 'greeting')):
            path = parser.get('sound', 'greeting')

    info('path = %s', path)

    return path

def get_denied_sound():
    # TODO: test
    parser.read('config.ini')
    path = parser.get('sound', 'granted')

    return path 

def play_sound(path):
    # TODO: re-enable and test in live environment
    info('playing sound')
    # run("/usr/bin/play", "-q", path, "trim", "0", "12")     
    return

def get_message(username):
    # TODO: implement
    parser.read('config.ini')
    message = parser.get('twitter', 'message')

    configpath = os.path.expanduser('~/.vuvuzela/config.ini')
    if (os.access(configpath, os.R_OK)):
        parser.read(configpath)
        if (parser.has_option('twitter', 'message')):
            message = parser.get('twitter', 'message')

    info('message = %s', message)

    return message 

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
            # TODO: re-enable in live environment
            #tapi.statuses.update(status=message)
            retry = 5
        except:
            warning('Problem updating twitter, retry attempt = ')

        retry = retry + 1
        time.sleep(5)

    if (retry == 4):
        error('Timed out updating twitter')

def get_connection():
    # vuvuzela.db should reside in /var/run/vuvuzela
    return sqlite3.connect('vuvuzela.db')

def log_entry(cardID, facilityID, flag, connection):
    # TODO: test 
    cursor = connection.cursor()
    # NOTE: this is order dependent on how the columns go in vuvuzela.entry_log
    params = (cardID, facilityID, flag, datetime.datetime.now())
    cursor.execute("insert into entry_log values(rowid, ?, ?, ?, ?)", params)

    connection.commit()

def has_access(flag):
    # TODO: test
    return (flag == "V") | (flag == "F")

def get_username(cardID, connection):
    # TODO: test
    cursor = connection.cursor()
    params = { 'cardID' : cardID }
    cursor.execute("select username from members where cardID = :cardID", params)
    username = cursor.fetchone()

    return username

def execute_granted_actions(username):
    # TODO: test 
    parser = ConfigParser.ConfigParser()
    soundpath = get_granted_sound(parser)
    message = get_message(username, parser)

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
    # facilityID should be '040'
    facilityID = line[2:4]
    cardID = line[5:]

    debug("flag = %s", %s)
    debug("facilityID = %s", %s)
    debug("cardID = %s", %s)

    log_entry(cardID, facilityID, flag, connection)

    if ( has_access(flag) ):
        info('member has access')
        
        username = get_username(cardID, connection)
        debug('username = %s', username)

        execute_granted_actions(username)
    else:
        info('member is denied access')
        execute_denied_actions() 

    connection.close()

    exit(0)

if __name__ == '__main__':
    main()
