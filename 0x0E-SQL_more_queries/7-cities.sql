-- creates a database
-- creates a tables
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id int UNIQUE NOT NULL AUTO_INCREMENT,
	state_id NOT NULL,
	name varchar(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(state_id)
	REFERENCES hbtn_0d_usa.states(id)
);
