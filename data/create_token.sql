CREATE TABLE IF NOT EXISTS token (
	tid INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	active BOOLEAN NOT NULL,
	engraving VARCHAR(255) NULL,
	locationid VARCHAR(255) NOT NULL,
	tokenid VARCHAR(255) NOT NULL
	);
