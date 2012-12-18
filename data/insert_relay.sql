INSERT INTO relay (zid, number, description) VALUES ((SELECT zid FROM zone WHERE name='00'), 1, 'Front Door');
INSERT INTO relay (zid, number, description) VALUES ((SELECT zid FROM zone WHERE name='06'), 1, 'Server Room Door');
INSERT INTO relay (zid, number, description) VALUES ((SELECT zid FROM zone WHERE name='11'), 1, 'Member Storage Door');
INSERT INTO relay (zid, number, description) VALUES ((SELECT zid FROM zone WHERE name='11'), 2, 'Tool Room Door');
