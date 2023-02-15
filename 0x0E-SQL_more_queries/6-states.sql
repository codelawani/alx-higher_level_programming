-- creates the database hbtn_0d_usa
-- and the table states (in the database hbtn_0d_usa)
CREATE DATABASE
	IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE
	IF NOT EXISTS states (
		id   INT          NOT NULL UNIQUE PRIMARY KEY 	
			 AUTO_INCREMENT,
		name VARCHAR(256) NOT NULL
	);
