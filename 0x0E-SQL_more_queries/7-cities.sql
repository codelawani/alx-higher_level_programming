-- creates the database hbtn_0d_usa
-- creates the database hbtn_0d_usa
CREATE DATABASE
	IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE
	IF NOT EXISTS cities (
		id        INT          NOT NULL UNIQUE PRIMARY KEY,
		state_id INT          NOT NULL,
		name      VARCHAR(256) NOT NULL,
		FOREIGN KEY (state_id) REFERENCES states(state_id)
	);
