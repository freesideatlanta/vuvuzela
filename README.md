
LDAP system and entries (TBD)
-----------------------------
- reinstall slapd on tammy
- create groups (admins, members, itstaff, inactives)
- test queries
- create LDIF entry for all freeside members
- custom schema for freeside member includes engraving, locationid, tokenid

MySQL database system
---------------------
    person (pid, full name, email, number)
    user (uid, login, pid)
    class (cid, name, description) *
    token (tid, active, engraving, locationid, tokenid) *
    zone (zid, name, description) 
    node (nid, zid, hostname)
    relay (rid, zid, number, description)
    user_class (ucid, uid, cid) *
    user_token (utid, uid, tid)
    class_node (cnid, cid, nid) *
    node_relay (nrid, nid, rid)
    log (lid, nid, when, tokenid, granted)

    * tables obsoleted when LDAP system manages groups

SQLite access control lists
---------------------------
    filename: <server>:/srv/<hostname>.db
    access (tokenid, number)

SQLite log
----------
    filename: <hostname>:/var/log/vuvuzela/<hostname>.db
    log (when, tokenid, granted)

vuvuzela (central server)
-------------------------
- query MySQL and/or LDAP to construct SQLite access control list
- read in the `<hostname>-log.db` log tables and import into central log
- [installation of python mysql libraries](http://codeinthehole.com/writing/how-to-set-up-mysql-for-python-on-ubuntu/)

vuvuzela (nodes)
----------------
- service runs on startup
- listens to COM port i/o for tokenid
- on tokenid read, query access table
- if in access table, for each number activate number relay
- record granted = true in log
- if not, record granted = false in log
- cron job periodically pulls from central server



