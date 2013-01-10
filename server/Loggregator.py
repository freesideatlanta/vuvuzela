import ConfigParser
import MySQLdb
import os
import sqlite3
import sys

from ConnectionManager import ConnectionManager

class Loggregator:
    def __init__(self, cm):
        self.cm = cm

    def aggregate(self):
        try:
            # query for the target hostname, relayid pairs
            query = self.query_targets()
            nodecursor = self.cm.db.cursor(MySQLdb.cursors.DictCursor)
            nodecursor.execute(query)

            for node in nodecursor:
                hostname = node["hostname"]
                relayid = node["relayid"]
                nid = node["nid"]
                rid = node["rid"]

                # connect to the sqlite log file for the node/relay and query the log
                nodelogpath = self.cm.logpath + hostname + "-" + str(relayid)
                nodelogfile = sqlite3.connect(nodelogpath)
                nodelogfile.row_factory = sqlite3.Row

                logcursor = nodelogfile.cursor()
                logquery = self.query_log()
                logcursor.execute(logquery)
                entries = logcursor.fetchall()

                # iterate through the sqlite log file for the node/relay
                for entry in entries:
                    time = entry["time"]
                    tokenid = entry["tokenid"]
                    granted = entry["granted"]

                    # insert a log entry into the master log
                    query = insert_entry(nid, rid, time, tokenid, granted)
                    insertcursor = self.cm.db.cursor()
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
        return "SELECT time, tokenid, granted FROM log";

    def insert_entry(self, nid, rid, time, tokenid, granted):
        return "INSERT INTO log (nid, rid, time, tokenid, granted) VALUES \
                (" + nid + ", " + rid + ", " + time + ", " + tokenid + ", " + granted + ")"

def main():
    cm = ConnectionManager()
    cm.connect()

    g = Loggregator(cm)
    g.aggregate()

    cm.close()

if __name__=='__main__':
    main()
