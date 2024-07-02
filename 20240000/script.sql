CREATE DATABASE IF NOT EXISTS egzondb;
USE egzondb;
CREATE TABLE employees (
  first_name varchar(45) DEFAULT NULL,
  last_name varchar(45) DEFAULT NULL
);

INSERT INTO employees (first_name, last_name) VALUES ('Egzon', 'Buzhala');