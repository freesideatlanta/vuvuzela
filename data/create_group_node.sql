CREATE TABLE IF NOT EXISTS group_node (
	gnid INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	gid INTEGER NOT NULL FOREIGN KEY REFERENCES group(gid),
	nid INTEGER NOT NULL FOREIGN KEY REFERENCES node(nid)
	);