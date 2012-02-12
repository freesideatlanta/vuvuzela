begin transaction;

create table entrylog(
	id INTEGER NOT NULL,
	striketime DATETIME NOT NULL,
	member_id NOT NULL);

commit;
