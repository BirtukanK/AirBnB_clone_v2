-- This script contains MySQL server preparation
-- A databas and new user
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT on performance_schema.* TO 'hbnb_dev'@'localhost';
Flush PRIVILEGES;
