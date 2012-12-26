import ConfigParser
import MySQLdb 
import os
import sqlite3
import sys

class Loggregator:
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

    def aggregate(self):
        try:
            # query for the target hostname, relayid pairs
            query = self.query_targets()
            nodecursor = self.db.cursor(MySQLdb.cursors.DictCursor)
            nodecursor.execute(query)

            for node in nodecursor:
                hostname = node["hostname"]
                relayid = node["relayid"]
                nid = node["nid"]
                rid = node["rid"]

                # connect to the sqlite log file for the node/relay and query the log
                nodelogpath = self.logpath + hostname + "-" + relayid
                nodelogfile = sqlite3.connect(nodelogpath)
                nodelogfile.row_factory = sqlite3.Row

                logcursor = nodelogfile.cursor()
                logquery = self.query_log()
                logcursor.execute(logquery)
                entries = logcursor.fetchall()

                # iterate through the sqlite log file for the node/relay
                for entry in entries:
                    when = entry["when"]
                    tokenid = entry["tokenid"]
                    granted = entry["granted"]

                    # insert a log entry into the master log
                    query = insert_entry(nid, rid, when, tokenid, granted)
                    insertcursor = self.db.cursor()
                    insertcursor.execute(query)

        except MySQLdb.Error, e:
            print(e)
            sys.exit(1)

    def query_targets(self):
        return "SELECT \
                c.cid AS groupid, name AS groupname, n.hostname, cnr.nid, r.number AS relayid, r.rid \
                FROM class c \
                JOIN class_node_relay cnr ON c.cid = cnr.cid \
                JOIN node n on n.nid = cnr.nid \
                JOIN relay r on r.rid = cnr.rid"

    def query_log(self):
        return "SELECT when, tokenid, granted FROM log";

    def insert_entry(self, nid, rid, when, tokenid, granted):
        return "INSERT INTO log (nid, rid, when, tokenid, granted) VALUES \
                (" + nid + ", " + rid + ", " + when + ", " + tokenid + ", " + granted + ")"

def main():
    g = Loggregator()
    g.connect()
    g.aggregate()
    g.close()

if __name__=='__main__':
    main()
