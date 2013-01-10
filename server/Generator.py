import ConfigParser
import MySQLdb
import os
import sqlite3
import sys

from ConnectionManager import ConnectionManager

class Generator:
    def __init__(self, cm):
        self.cm = cm

    def generate(self):
        try:
            # select the targets
            query = self.query_targets()
            groupcursor = self.cm.db.cursor(MySQLdb.cursors.DictCursor)
            groupcursor.execute(query)

            # iterate through the targets (groupid, groupname, description, hostname, nodeid, relayid)
            for group in groupcursor:
                groupid = group["groupid"]
                hostname = group["hostname"]
                nodeid = group["nodeid"]
                relayid = group["relayid"]

                filename = self.create_acl(hostname, relayid)

                query = self.query_acl(groupid)
                aclcursor = self.cm.db.cursor(MySQLdb.cursors.DictCursor)
                aclcursor.execute(query)

                self.insert_aclentries(filename, aclcursor)

                self.create_logfile(hostname, relayid)

        except MySQLdb.Error, e:
            print(e)
            sys.exit(1)

    def create_acl(self, hostname, relayid):
        # generate sqlite file hostname-relayid.db with access, log tables
        print("generating ACL: " + hostname + "-" + str(relayid) + ".db")
        filename = self.cm.aclpath + hostname + "-" + str(relayid) + ".db"

        try:
            acl = sqlite3.connect(filename)
            cursor = acl.cursor()
            query = self.create_access()
            cursor.execute(query)
        except sqlite3.Error, e:
            print(e)
            sys.exit(1)
        finally:
            if acl:
                acl.close()

        return filename

    def insert_aclentries(self, filename, aclcursor):
        # insert the entries into the access table
        acl = None
        try:
            acl = sqlite3.connect(filename)
            cursor = acl.cursor()

            for entry in aclcursor:
                locationid = entry["locationid"]
                tokenid = entry["tokenid"]

                query = self.insert_access(locationid, tokenid)
                cursor.execute(query)

        except sqlite3.Error, e:
            print(e)
            sys.exit(1)
        finally:
            if acl:
                acl.close()

    def create_logfile(self, hostname, relayid):
        logfile = None
        try:
            filename = self.cm.logpath + hostname + "-" + str(relayid)
            logfile = sqlite3.connect(filename)
            cursor = logfile.cursor()
            query = self.create_log()
            cursor.execute(query)
        except sqlite3.Error, e:
            print(e)
            sys.exit(1)
        finally:
            if logfile:
                logfile.close()

    def query_targets(self):
        return "SELECT \
                c.cid AS groupid, name AS groupname, n.hostname, cnr.nid AS nodeid, r.number AS relayid \
                FROM class c \
                JOIN class_node_relay cnr ON c.cid = cnr.cid \
                JOIN node n on n.nid = cnr.nid \
                JOIN relay r on r.rid = cnr.rid"

    def query_acl(self, groupid):
        return "SELECT \
                login, c.cid as groupid, name AS groupname, locationid, tokenid \
                FROM user u \
                JOIN user_class uc ON u.uid = uc.uid \
                JOIN class c ON c.cid = uc.cid \
                JOIN user_token ut ON u.uid = ut.uid \
                JOIN token t ON t.tid = ut.tid \
                WHERE c.cid = " + str(groupid)

    def create_access(self):
        return "CREATE TABLE access(tokenid TEXT)"

    def insert_access(self, locationid, tokenid):
        return "INSERT INTO access VALUES (" + locationid + tokenid + ")"

    def create_log(self):
        return "CREATE TABLE log (time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, tokenid TEXT, granted INT)"


def main():
    cm = ConnectionManager()
    cm.connect()

    g = Generator(cm)
    g.generate()

    cm.close()

if __name__=='__main__':
    main()
