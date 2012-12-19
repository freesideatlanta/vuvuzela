import ConfigParser
import MySQLdb 
import os
import sys

class Generator:
    def __init__(self):
        self.db = None

        parser = ConfigParser.ConfigParser()
        # override the database credentials with the vuvuzela user configuration
        local = os.path.expanduser('~/.vuvuzela/configuration.ini')
        parser.read(['configuration.ini', local])

        if (parser.has_section('datastore')):
            self.hostname = parser.get('datastore', 'hostname')
            self.username = parser.get('datastore', 'username')
            self.password = parser.get('datastore', 'password')
            self.database = parser.get('datastore', 'database')

    def connect(self):
        try:
            self.db = MySQLdb.connect(host=self.hostname, user=self.username, passwd=self.password, db=self.database)
        except MySQLdb.Error, e:
            print(e)
            sys.exit(1)

    def close(self):
        if self.db:
            self.db.close()

    def generate(self):
        try:
            # select the targets
            query = self.query_targets()
            groupcursor = self.db.cursor(MySQLdb.cursors.DictCursor)
            groupcursor.execute(query)

            # iterate through the targets (groupid, groupname, description, hostname, nodeid, relayid)
            for group in groupcursor:
                groupid = group["groupid"]
                hostname = group["hostname"]
                nodeid = group["nodeid"]
                relayid = group["relayid"]

                self.create_acl(hostname, relayid)

                query = self.query_acl(groupid)
                aclcursor = self.db.cursor(MySQLdb.cursors.DictCursor)
                aclcursor.execute(query)

                for entry in aclcursor:
                    locationid = entry["locationid"]
                    tokenid = entry["tokenid"]

                    self.insert_aclentry(locationid, tokenid)


        except MySQLdb.Error, e:
            print(e)
            sys.exit(1)

    def create_acl(self, hostname, relayid):
        # TODO: generate sqlite file hostname-relayid.db with access, log tables
        print("generating ACL: " + hostname + "-" + str(relayid) + ".db")

    def insert_aclentry(self, locationid, tokenid):
        # TODO: insert the entry into the access table
        print(locationid + tokenid)
        
    def query_targets(self):
        return "SELECT \
                c.cid AS groupid, name AS groupname, description, n.hostname, cnr.nid AS nodeid, cnr.rid AS relayid \
                FROM class c \
                JOIN class_node_relay cnr ON c.cid = cnr.cid \
                JOIN node n on n.nid = cnr.nid"
    
    def query_acl(self, groupid):
        return "SELECT \
                login, c.cid as groupid, name AS groupname, description, locationid, tokenid \
                FROM user u \
                JOIN user_class uc ON u.uid = uc.uid \
                JOIN class c ON c.cid = uc.cid \
                JOIN user_token ut ON u.uid = ut.uid \
                JOIN token t ON t.tid = ut.tid \
                WHERE c.cid = " + str(groupid)


def main():
    g = Generator()
    g.connect()
    g.generate()
    g.close()

if __name__=='__main__':
    main()
