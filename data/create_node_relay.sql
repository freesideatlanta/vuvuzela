CREATE TABLE IF NOT EXISTS node_relay (
	nrid INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	nid INTEGER NOT NULL FOREIGN KEY REFERENCES node(nid),
	rid INTEGER NOT NULL FOREIGN KEY REFERENCES relay(rid)
	);
