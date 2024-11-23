-- SCHEMA
Create table If Not Exists cinema (id int, movie varchar(255), description varchar(255), rating DECIMAL(2, 1));
Truncate table cinema;
insert into cinema (id, movie, description, rating) values ('1', 'War', 'great 3D', '8.9');
insert into cinema (id, movie, description, rating) values ('2', 'Science', 'fiction', '8.5');
insert into cinema (id, movie, description, rating) values ('3', 'irish', 'boring', '6.2');
insert into cinema (id, movie, description, rating) values ('4', 'Ice song', 'Fantacy', '8.6');
insert into cinema (id, movie, description, rating) values ('5', 'House card', 'Interesting', '9.1');

-- SOLUTION 1 calculate mod using floor & basic arithmetic
SELECT *
FROM cinema c
WHERE c.description <> 'boring' AND c.id-2*FLOOR(c.id/2)=1
ORDER BY c.rating DESC;

-- SOLUTION 2 mod function
SELECT *
FROM cinema c
WHERE c.description != 'boring' AND MOD(c.id,2)=1
ORDER BY c.rating DESC;


-- SOLUTION 3 mod operator
SELECT *
FROM cinema c
WHERE c.description != 'boring' AND (c.id%2)=1
ORDER BY c.rating DESC;
