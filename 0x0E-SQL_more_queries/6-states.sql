-- creates a database
-- creates a tables
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id int UNIQUE NOT NULL AUTO_INCREMENT, name varchar(256) NOT NULL, PRIMARY KEY (id));
