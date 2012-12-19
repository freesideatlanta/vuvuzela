-- front door
INSERT INTO class_node_relay (cid, nid, rid) VALUES (
	(SELECT cid FROM class WHERE name='members'), 
	(SELECT nid FROM node WHERE hostname='joker'), 
	(SELECT r.rid FROM node n JOIN node_relay nr ON n.nid = nr.nid JOIN relay r ON r.rid = nr.rid 
		WHERE r.number=1 AND n.hostname='joker')
);
-- server room door
INSERT INTO class_node_relay (cid, nid, rid) VALUES (
	(SELECT cid FROM class WHERE name='itstaff'), 
	(SELECT nid FROM node WHERE hostname='riddler'), 
	(SELECT r.rid FROM node n JOIN node_relay nr ON n.nid = nr.nid JOIN relay r ON r.rid = nr.rid 
		WHERE r.number=1 AND n.hostname='riddler')
);
-- member storage door
INSERT INTO class_node_relay (cid, nid, rid) VALUES (
	(SELECT cid FROM class WHERE name='members'), 
	(SELECT nid FROM node WHERE hostname='catwoman'), 
	(SELECT r.rid FROM node n JOIN node_relay nr ON n.nid = nr.nid JOIN relay r ON r.rid = nr.rid 
		WHERE r.number=1 AND n.hostname='catwoman')
);
-- tool room door
INSERT INTO class_node_relay (cid, nid, rid) VALUES (
	(SELECT cid FROM class WHERE name='members'), 
	(SELECT nid FROM node WHERE hostname='catwoman'), 
	(SELECT r.rid FROM node n JOIN node_relay nr ON n.nid = nr.nid JOIN relay r ON r.rid = nr.rid 
		WHERE r.number=2 AND n.hostname='catwoman')
);
