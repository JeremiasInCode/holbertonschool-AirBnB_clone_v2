-- Create the database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create User if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant hbnb_test the privileges on the database hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant hbnb_test SELECT privileges on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush to apply changes
FLUSH PRIVILEGES;