begin transaction;

create table members_backup(id, cardID, alias, email);
insert into members_backup 
	select id, substr(cardID, 4, 7), alias, email 
	from members;
drop table members;

create table members (
	id INTEGER NOT NULL, 
	card_id VARCHAR(5) NOT NULL, 
	username VARCHAR(32) NOT NULL);
insert into members 
	select id, cardID, 'nobody' 
	from members_backup;

create table contacts (
	id INTEGER NOT NULL,
	card_id VARCHAR(5) NOT NULL,
	alias VARCHAR(32),
	email VARCHAR(255));
insert into contacts
	select rowid, cardID, alias, email 
	from members_backup;

drop table members_backup;

commit;
