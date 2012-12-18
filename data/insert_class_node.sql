INSERT INTO class_node (cid, nid) VALUES ((SELECT cid FROM class WHERE name='members'), (SELECT nid FROM node WHERE hostname='joker'));
INSERT INTO class_node (cid, nid) VALUES ((SELECT cid FROM class WHERE name='itstaff'), (SELECT nid FROM node WHERE hostname='riddler'));
INSERT INTO class_node (cid, nid) VALUES ((SELECT cid FROM class WHERE name='members'), (SELECT nid FROM node WHERE hostname='catwoman'));
