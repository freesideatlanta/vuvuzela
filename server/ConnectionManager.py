import ConfigParser
import MySQLdb 
import os
import sqlite3
import sys

class ConnectionManager:
    def __init__(self):
        self.db = None

        parser = ConfigParser.ConfigParser()
        local = os.path.expanduser('~/.vuvuzela/configuration.ini')
        parser.read(['configuration.ini', local])

        if (parser.has_section('datastore')):
            self.hostname = parser.get('datastore', 'hostname')
            self.username = parser.get('datastore', 'username')
            self.password = parser.get('datastore', 'password')
            self.database = parser.get('datastore', 'database')

        if (parser.has_section('targets')):
            self.aclpath = parser.get('targets', 'aclpath')
            self.logpath = parser.get('targets', 'logpath')

    def connect(self):
        try:
            self.db = MySQLdb.connect(host=self.hostname, user=self.username, passwd=self.password, db=self.database)
        except MySQLdb.Error, e:
            print(e)
            sys.exit(1)

    def close(self):
        if self.db:
            self.db.close()

def main():
    cm = ConnectionManager()
    cm.connect()
    print(cm.hostname + " " + cm.database + " ")
    cm.close()

if __name__=='__main__':
    main()
