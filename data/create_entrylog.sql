begin transaction;

create table entrylog(
	id INTEGER NOT NULL,
	card_id VARCHAR(8) NOT NULL,
	location_id VARCHAR(3) NOT NULL,
	strike_flag CHARACTER(1) NOT NULL,
	strike_time DATETIME NOT NULL);

commit;
