INSERT INTO node_relay (nid, rid) VALUES ((SELECT nid FROM node WHERE hostname='joker'), (SELECT rid FROM relay WHERE description='Front Door'));
INSERT INTO node_relay (nid, rid) VALUES ((SELECT nid FROM node WHERE hostname='riddler'), (SELECT rid FROM relay WHERE description='Server Room Door'));
INSERT INTO node_relay (nid, rid) VALUES ((SELECT nid FROM node WHERE hostname='catwoman'), (SELECT rid FROM relay WHERE description='Member Storage Door'));
INSERT INTO node_relay (nid, rid) VALUES ((SELECT nid FROM node WHERE hostname='catwoman'), (SELECT rid FROM relay WHERE description='Tool Room Door'));
