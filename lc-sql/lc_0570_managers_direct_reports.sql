SET client_min_messages TO WARNING;

-- -- SCHEMA
-- Drop table Employee;
Create table If Not Exists Employee (id int, name varchar(255), department varchar(255), managerId int);
Truncate table Employee;

insert into Employee (id, name, department, managerId) values ('101', 'John', 'A', NULL);
insert into Employee (id, name, department, managerId) values ('102', 'Dan', 'A', '101');
insert into Employee (id, name, department, managerId) values ('103', 'James', 'A', '101');
insert into Employee (id, name, department, managerId) values ('104', 'Amy', 'A', '101');
insert into Employee (id, name, department, managerId) values ('105', 'Anne', 'A', '101');
insert into Employee (id, name, department, managerId) values ('106', 'Ron', 'B', '101');
insert into Employee (id, name, department, managerId) values ('107', 'John', 'A', NULL);
insert into Employee (id, name, department, managerId) values ('108', 'Dan', 'A', '107');
insert into Employee (id, name, department, managerId) values ('109', 'James', 'A', '107');
insert into Employee (id, name, department, managerId) values ('110', 'Amy', 'A', '107');
insert into Employee (id, name, department, managerId) values ('111', 'Anne', 'A', '107');
insert into Employee (id, name, department, managerId) values ('112', 'Ron', 'B', '107');

-- | id  | name  | department | managerId |
-- | --- | ----- | ---------- | --------- |
-- | 101 | John  | A          | null      |
-- | 102 | Dan   | A          | 101       |
-- | 103 | James | A          | 101       |
-- | 104 | Amy   | A          | 101       |
-- | 105 | Anne  | A          | 101       |
-- | 106 | Ron   | B          | 101       |
-- | 111 | John  | A          | null      |
-- | 112 | Dan   | A          | 111       |
-- | 113 | James | A          | 111       |
-- | 114 | Amy   | A          | 111       |
-- | 115 | Anne  | A          | 111       |
-- | 116 | Ron   | B          | 111       |

-- SOLUTION
SELECT name
FROM (
    SELECT e1.id, e1.name
    FROM Employee AS e1
    INNER JOIN Employee AS e2 ON e1.id=e2.managerId 
    GROUP BY e1.id, e1.name
    HAVING COUNT(*) >= 5);
