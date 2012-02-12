begin transaction;

create table members_backup(id, cardID, alias);
insert into members_backup select id, cardID, alias from members;
drop table members;

create table members(
	id INTEGER NOT NULL, 
	cardID VARCHAR(8) NOT NULL, 
	locationID VARCHAR(3) NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	alias VARCHAR(32));
insert into members select id, cardID, '000', 'nobody', alias from members_backup;
drop table members_backup;

commit;
