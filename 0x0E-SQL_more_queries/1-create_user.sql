-- creates the MySQL server user user_0d_1
-- user_0d_1 should have all privilege
CREATE USER
	IF NOT EXISTS 'user_0d_1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
	ON *.*
	TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
