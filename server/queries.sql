
-- get a list of node, relay related to class
SELECT 
	c.cid AS groupid,
	name AS groupname,
	description,
	cnr.nid AS nodeid,
	cnr.rid AS relayid
FROM class c
JOIN class_node_relay cnr ON c.cid = cnr.cid;
-- used first to get a list of (node, relay) pair to generate an ACL from (class)

-- for naming targets of the ACL creation, ex. joker-1.db
SELECT 
    n.nid AS nodeid,
	hostname AS node, 
	z.name AS zone, 
	z.description, 
	number AS relay, 
	r.description AS target 
FROM node n 
JOIN node_relay nr ON n.nid = nr.nid 
JOIN relay r ON r.rid = nr.rid 
JOIN zone z ON z.zid = n.zid
WHERE n.nid = <nodeid>
AND r.rid = <relayid>;
-- supply <nodeid> and <relayid> to get the hostname and relay number

-- identifying the ACLs by group
SELECT 
	login, 
	c.cid as groupid,
	name AS groupname, 
	description, 
	locationid, 
	tokenid 
FROM user u 
JOIN user_class uc ON u.uid = uc.uid 
JOIN class c ON c.cid = uc.cid 
JOIN user_token ut ON u.uid = ut.uid 
JOIN token t ON t.tid = ut.tid
WHERE c.cid = <groupid>;
-- supply <groupid> to retrieve the ACL for that group

