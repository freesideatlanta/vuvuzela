INSERT INTO node (zid, hostname) VALUES ((SELECT zid FROM zone WHERE name='00'), 'joker');
INSERT INTO node (zid, hostname) VALUES ((SELECT zid FROM zone WHERE name='06'), 'riddler');
INSERT INTO node (zid, hostname) VALUES ((SELECT zid FROM zone WHERE name='11'), 'catwoman');
