-- Create a databse [hbnb_dev_db] --
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a new User [hbnb_dev] in localhost
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY  'hbnb_dev_pwd';

-- Grant user all privileges on the database [hbnb_dev_db]
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
