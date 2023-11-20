-- Create the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create User if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant hbnb_dev the privileges on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant hbnb_dev SELECT privileges on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush to apply changes
FLUSH PRIVILEGES;