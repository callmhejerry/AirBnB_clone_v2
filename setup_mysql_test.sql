-- Create a database [hbnb_test_db]
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user [hbnb_test] in localhost
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges on the database [hbnb_test_db]
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privileges on the database peformance_Schema and only this database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
