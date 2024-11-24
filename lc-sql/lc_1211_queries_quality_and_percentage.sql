-- SCHEMA
Create table If Not Exists Queries (query_name varchar(30), result varchar(50), position int, rating int);
Truncate table Queries;
insert into Queries (query_name, result, position, rating) values ('Dog', 'Golden Retriever', '1', '5');
insert into Queries (query_name, result, position, rating) values ('Dog', 'German Shepherd', '2', '5');
insert into Queries (query_name, result, position, rating) values ('Dog', 'Mule', '200', '1');
insert into Queries (query_name, result, position, rating) values ('Cat', 'Shirazi', '5', '2');
insert into Queries (query_name, result, position, rating) values ('Cat', 'Siamese', '3', '3');
insert into Queries (query_name, result, position, rating) values ('Cat', 'Sphynx', '7', '4');

-- SOLUTION
SELECT
    q.query_name,
    ROUND(AVG(1. * q.rating/q.position), 2) as quality,
    ROUND(100. * COUNT(q.rating) FILTER (WHERE q.rating < 3) / COUNT(*), 2) as poor_query_percentage
FROM Queries q
WHERE q.query_name IS NOT NULL
GROUP BY q.query_name;
