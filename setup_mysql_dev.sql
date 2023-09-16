-- create a database hbnb_dev_db
-- create user hbnb_dev

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `preformance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
