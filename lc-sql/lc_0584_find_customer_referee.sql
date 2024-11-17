SET client_min_messages TO WARNING;

-- SCHEMA
CREATE TABLE IF NOT EXISTS Customer (id INT, name VARCHAR(25), referee_id INT);
TRUNCATE TABLE Customer;
INSERT INTO Customer (id, name, referee_id) VALUES ('1', 'Will', NULL);
INSERT INTO Customer (id, name, referee_id) VALUES ('2', 'Jane', NULL);
INSERT INTO Customer (id, name, referee_id) VALUES ('3', 'Alex', '2');
INSERT INTO Customer (id, name, referee_id) VALUES ('4', 'Bill', NULL);
INSERT INTO Customer (id, name, referee_id) VALUES ('5', 'Zack', '1');
INSERT INTO Customer (id, name, referee_id) VALUES ('6', 'Mark', '2');

-- SOLUTION
SELECT name
FROM Customer
WHERE referee_id IS NULL OR referee_id != 2;
