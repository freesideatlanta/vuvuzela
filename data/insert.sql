INSERT INTO person (name, email, number) VALUES ('Alan Fay', 'emptyset@gmail.com', '404-861-0905');
INSERT INTO person (name, email, number) VALUES ('Ben Bradley', 'ben_n_bradley@etcmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Brent Cerrato', 'methuse@gmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Brian Cribbs', 'quadmasta@hotmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Buddy Smith', 'nullset@gmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Cam Kilgore', 'ghostfreeman@gmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Chris Moore', 'pacsman2005@gmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Donald Hoefer', 'fatpandasays@gmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Donald Mead', 'dmm@yak.net', null);
INSERT INTO person (name, email, number) VALUES ('E Joseph Wertz', 'e.joseph.wertz@gmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Eldon', 'npcomp@npcomp.net', null);
INSERT INTO person (name, email, number) VALUES ('H Preston Ladds', 'householdwords@gmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Igor Kondratyuk', 'vigor.rigor.igor@gmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Joe Koberg', 'joe@koberg.us', null);
INSERT INTO person (name, email, number) VALUES ('Joshua Oster-Morris', 'josh@craftycoder.com', null);
INSERT INTO person (name, email, number) VALUES ('Karen Sanders', 'acmepost@yahoo.com', null);
INSERT INTO person (name, email, number) VALUES ('Kirk Stephens', 'k4stephens@gmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Mark Luffel', 'markluffel@gmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Newton White', 'konewt@comcast.net', null);
INSERT INTO person (name, email, number) VALUES ('Nick Giovinco', 'ngiovinco@gmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Paul Firnschild', 'paul@firnschild.com', null);
INSERT INTO person (name, email, number) VALUES ('Randall Bollig', 'ghost@uxch.com', null);
INSERT INTO person (name, email, number) VALUES ('Randy Farmer', 'randy.farmer@gmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Robert Graham', 'rpgraham84@gmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Scott McGraw', 'scott.mcgraw@gatech.edu', null);
INSERT INTO person (name, email, number) VALUES ('Sean Kennedy', 'seanfkennedy@gmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Sean McNealy', 'seanmcnealy@gmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Slade Stricklin', 'sladestricklin@gmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Steven Sutton', 'ssutton4455@gmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Wallace Murphy', 'myonen.mc.ca@gmail.com', null);
INSERT INTO person (name, email, number) VALUES ('Wayne Salhany', 'waynesalhany@cythink.com', null);
INSERT INTO person (name, email, number) VALUES ('Zachary Alig', 'zachalig@gmail.com', null);
INSERT INTO user (login, pid) VALUES ('emptyset', (SELECT pid FROM person WHERE email='emptyset@gmail.com'));
INSERT INTO user (login, pid) VALUES ('ben.bradley', (SELECT pid FROM person WHERE email='ben_n_bradley@etcmail.com'));
INSERT INTO user (login, pid) VALUES ('brent.cerrato', (SELECT pid FROM person WHERE email='methuse@gmail.com'));
INSERT INTO user (login, pid) VALUES ('cribbsb', (SELECT pid FROM person WHERE email='quadmasta@hotmail.com'));
INSERT INTO user (login, pid) VALUES ('nullset', (SELECT pid FROM person WHERE email='nullset@gmail.com'));
INSERT INTO user (login, pid) VALUES ('thrillgore', (SELECT pid FROM person WHERE email='ghostfreeman@gmail.com'));
INSERT INTO user (login, pid) VALUES ('chris.moore', (SELECT pid FROM person WHERE email='pacsman2005@gmail.com'));
INSERT INTO user (login, pid) VALUES ('panda', (SELECT pid FROM person WHERE email='fatpandasays@gmail.com'));
INSERT INTO user (login, pid) VALUES ('donald.mead', (SELECT pid FROM person WHERE email='dmm@yak.net'));
INSERT INTO user (login, pid) VALUES ('e.joseph.wertz', (SELECT pid FROM person WHERE email='e.joseph.wertz@gmail.com'));
INSERT INTO user (login, pid) VALUES ('npcomp', (SELECT pid FROM person WHERE email='npcomp@npcomp.net'));
INSERT INTO user (login, pid) VALUES ('h.preston.ladds', (SELECT pid FROM person WHERE email='householdwords@gmail.com'));
INSERT INTO user (login, pid) VALUES ('ferris', (SELECT pid FROM person WHERE email='vigor.rigor.igor@gmail.com'));
INSERT INTO user (login, pid) VALUES ('joe', (SELECT pid FROM person WHERE email='joe@koberg.us'));
INSERT INTO user (login, pid) VALUES ('josh.ostermorris', (SELECT pid FROM person WHERE email='josh@craftycoder.com'));
INSERT INTO user (login, pid) VALUES ('acmepost', (SELECT pid FROM person WHERE email='acmepost@yahoo.com'));
INSERT INTO user (login, pid) VALUES ('kirk', (SELECT pid FROM person WHERE email='k4stephens@gmail.com'));
INSERT INTO user (login, pid) VALUES ('mark.luffel', (SELECT pid FROM person WHERE email='markluffel@gmail.com'));
INSERT INTO user (login, pid) VALUES ('newton.white', (SELECT pid FROM person WHERE email='konewt@comcast.net'));
INSERT INTO user (login, pid) VALUES ('nick.giovinco', (SELECT pid FROM person WHERE email='ngiovinco@gmail.com'));
INSERT INTO user (login, pid) VALUES ('paul.firnschild', (SELECT pid FROM person WHERE email='paul@firnschild.com'));
INSERT INTO user (login, pid) VALUES ('randall.bollig', (SELECT pid FROM person WHERE email='ghost@uxch.com'));
INSERT INTO user (login, pid) VALUES ('randy.farmer', (SELECT pid FROM person WHERE email='randy.farmer@gmail.com'));
INSERT INTO user (login, pid) VALUES ('devrg0', (SELECT pid FROM person WHERE email='rpgraham84@gmail.com'));
INSERT INTO user (login, pid) VALUES ('scott.mcgraw', (SELECT pid FROM person WHERE email='scott.mcgraw@gatech.edu'));
INSERT INTO user (login, pid) VALUES ('sean.kennedy', (SELECT pid FROM person WHERE email='seanfkennedy@gmail.com'));
INSERT INTO user (login, pid) VALUES ('sean.mcnealy', (SELECT pid FROM person WHERE email='seanmcnealy@gmail.com'));
INSERT INTO user (login, pid) VALUES ('slade', (SELECT pid FROM person WHERE email='sladestricklin@gmail.com'));
INSERT INTO user (login, pid) VALUES ('steamboat', (SELECT pid FROM person WHERE email='ssutton4455@gmail.com'));
INSERT INTO user (login, pid) VALUES ('wallace.murphy', (SELECT pid FROM person WHERE email='myonen.mc.ca@gmail.com'));
INSERT INTO user (login, pid) VALUES ('wayne.salhany', (SELECT pid FROM person WHERE email='waynesalhany@cythink.com'));
INSERT INTO user (login, pid) VALUES ('zach.alig', (SELECT pid FROM person WHERE email='zachalig@gmail.com'));

INSERT INTO class (name, description) VALUES ('members', 'Freeside Atlanta Members');
INSERT INTO class (name, description) VALUES ('itstaff', 'Freeside IT Staff');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (true, '0001110497', '016', '61921');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (true, '0001115701', '017', '01589');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (true, '0001112357', '016', '63781');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (true, null, '037', '55267');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (true, '0001108877', '016', '60301');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (true, '0001112766', '016', '64190');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (true, '0001117440', '017', '03328');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (true, '0001107321', '016', '58745');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (true, '0001118667', '017', '04555');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (true, '0001115132', '017', '01020');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (true, '0001115485', '017', '01373');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (true, '0001116364', '017', '02252');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (true, '0001109442', '016', '60866');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (true, '0001117953', '017', '03841');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (true, '0001108324', '016', '59748');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (true, '0001111268', '016', '62692');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (false, '0001111023', '016', '62447');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (true, '0001112650', '016', '64074');
INSERT INTO token (active, engraving, locationid, tokenid) VALUES (true, '0001109365', '016', '60789');
INSERT INTO zone (name, description) VALUES ('00', 'Welcome');
INSERT INTO zone (name, description) VALUES ('01', '3D Printing');
INSERT INTO zone (name, description) VALUES ('02', 'TBD');
INSERT INTO zone (name, description) VALUES ('03', 'Electronics Lab');
INSERT INTO zone (name, description) VALUES ('04', 'Kitchen');
INSERT INTO zone (name, description) VALUES ('05', 'Classroom');
INSERT INTO zone (name, description) VALUES ('06', 'Server Room');
INSERT INTO zone (name, description) VALUES ('07', 'Auditorium');
INSERT INTO zone (name, description) VALUES ('08', 'Parts Storage');
INSERT INTO zone (name, description) VALUES ('09', 'Darkroom');
INSERT INTO zone (name, description) VALUES ('10', 'TBD');
INSERT INTO zone (name, description) VALUES ('11', 'Member Storage');
INSERT INTO zone (name, description) VALUES ('12', 'Project Storage');
INSERT INTO zone (name, description) VALUES ('13', 'Loft');
INSERT INTO zone (name, description) VALUES ('14', 'Tool Room');
INSERT INTO zone (name, description) VALUES ('15', 'Woodshop');
INSERT INTO zone (name, description) VALUES ('16', 'CNC Lab');
INSERT INTO zone (name, description) VALUES ('17', 'Garage');
INSERT INTO zone (name, description) VALUES ('18', 'Workstations');
INSERT INTO zone (name, description) VALUES ('19', 'Safety');
INSERT INTO zone (name, description) VALUES ('20', 'Workspace');
INSERT INTO zone (name, description) VALUES ('21', 'Attic');
INSERT INTO node (zid, hostname) VALUES ((SELECT zid FROM zone WHERE name='00'), 'joker');
INSERT INTO node (zid, hostname) VALUES ((SELECT zid FROM zone WHERE name='06'), 'riddler');
INSERT INTO node (zid, hostname) VALUES ((SELECT zid FROM zone WHERE name='11'), 'catwoman');
INSERT INTO relay (zid, number, description) VALUES ((SELECT zid FROM zone WHERE name='00'), 1, 'Front Door');
INSERT INTO relay (zid, number, description) VALUES ((SELECT zid FROM zone WHERE name='06'), 1, 'Server Room Door');
INSERT INTO relay (zid, number, description) VALUES ((SELECT zid FROM zone WHERE name='11'), 1, 'Member Storage Door');
INSERT INTO relay (zid, number, description) VALUES ((SELECT zid FROM zone WHERE name='14'), 2, 'Tool Room Door');
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='quadmasta@hotmail.com'), (SELECT tid FROM token WHERE tokenid='61921'));
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='vigor.rigor.igor@gmail.com'), (SELECT tid FROM token WHERE tokenid='01589'));
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='emptyset@gmail.com'), (SELECT tid FROM token WHERE tokenid='63781'));
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='myonen.mc.ca@gmail.com'), (SELECT tid FROM token WHERE tokenid='55267'));
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='scott.mcgraw@gatech.edu'), (SELECT tid FROM token WHERE tokenid='60301'));
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='paul@firnschild.com'), (SELECT tid FROM token WHERE tokenid='64190'));
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='waynesalhany@cythink.com'), (SELECT tid FROM token WHERE tokenid='03328'));
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='pacsman2005@gmail.com'), (SELECT tid FROM token WHERE tokenid='58745'));
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='npcomp@npcomp.net'), (SELECT tid FROM token WHERE tokenid='04555'));
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='seanfkennedy@gmail.com'), (SELECT tid FROM token WHERE tokenid='01020'));
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='randy.farmer@gmail.com'), (SELECT tid FROM token WHERE tokenid='01373'));
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='ghostfreeman@gmail.com'), (SELECT tid FROM token WHERE tokenid='02252'));
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='ben_n_bradley@etcmail.com'), (SELECT tid FROM token WHERE tokenid='60866'));
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='dmm@yak.net'), (SELECT tid FROM token WHERE tokenid='03841'));
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='ghost@uxch.com'), (SELECT tid FROM token WHERE tokenid='59748'));
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='ssutton4455@gmail.com'), (SELECT tid FROM token WHERE tokenid='62692'));
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='nullset@gmail.com'), (SELECT tid FROM token WHERE tokenid='62447'));
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='fatpandasays@gmail.com'), (SELECT tid FROM token WHERE tokenid='64074'));
INSERT INTO user_token (uid, tid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='methuse@gmail.com'), (SELECT tid FROM token WHERE tokenid='60789'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='ben_n_bradley@etcmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='methuse@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='ghostfreeman@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='joe@koberg.us'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='npcomp@npcomp.net'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='fatpandasays@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='emptyset@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='quadmasta@hotmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='nullset@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='pacsman2005@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='dmm@yak.net'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='e.joseph.wertz@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='householdwords@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='vigor.rigor.igor@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='josh@craftycoder.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='acmepost@yahoo.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='k4stephens@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='markluffel@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='konewt@comcast.net'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='ngiovinco@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='paul@firnschild.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='ghost@uxch.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='randy.farmer@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='rpgraham84@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='scott.mcgraw@gatech.edu'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='seanfkennedy@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='seanmcnealy@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='sladestricklin@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='ssutton4455@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='myonen.mc.ca@gmail.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='waynesalhany@cythink.com'), (SELECT cid FROM class WHERE name='members'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='zachalig@gmail.com'), (SELECT cid FROM class WHERE name='members'));

INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='ghostfreeman@gmail.com'), (SELECT cid FROM class WHERE name='itstaff'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='joe@koberg.us'), (SELECT cid FROM class WHERE name='itstaff'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='npcomp@npcomp.net'), (SELECT cid FROM class WHERE name='itstaff'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='fatpandasays@gmail.com'), (SELECT cid FROM class WHERE name='itstaff'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='emptyset@gmail.com'), (SELECT cid FROM class WHERE name='itstaff'));
INSERT INTO user_class (uid, cid) VALUES ((SELECT uid FROM user JOIN person ON user.pid = person.pid WHERE person.email='quadmasta@hotmail.com'), (SELECT cid FROM class WHERE name='itstaff'));
INSERT INTO class_node (cid, nid) VALUES ((SELECT cid FROM class WHERE name='members'), (SELECT nid FROM node WHERE hostname='joker'));
INSERT INTO class_node (cid, nid) VALUES ((SELECT cid FROM class WHERE name='itstaff'), (SELECT nid FROM node WHERE hostname='riddler'));
INSERT INTO class_node (cid, nid) VALUES ((SELECT cid FROM class WHERE name='members'), (SELECT nid FROM node WHERE hostname='catwoman'));
INSERT INTO node_relay (nid, rid) VALUES ((SELECT nid FROM node WHERE hostname='joker'), (SELECT rid FROM relay WHERE description='Front Door'));
INSERT INTO node_relay (nid, rid) VALUES ((SELECT nid FROM node WHERE hostname='riddler'), (SELECT rid FROM relay WHERE description='Server Room Door'));
INSERT INTO node_relay (nid, rid) VALUES ((SELECT nid FROM node WHERE hostname='catwoman'), (SELECT rid FROM relay WHERE description='Member Storage Door'));
INSERT INTO node_relay (nid, rid) VALUES ((SELECT nid FROM node WHERE hostname='catwoman'), (SELECT rid FROM relay WHERE description='Tool Room Door'));
