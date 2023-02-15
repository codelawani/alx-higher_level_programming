-- creates the table unique_id
CREATE TABLE
	IF NOT EXISTS unique_id (
		id   INT		  DEFAULT 1 unique,
		name VARCHAR(256)
	);
