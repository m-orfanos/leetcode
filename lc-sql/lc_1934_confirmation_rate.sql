SET client_min_messages TO WARNING;

-- SCHEMA
CREATE TYPE confirmation_status AS ENUM('confirmed','timeout');
Create table If Not Exists Signups (user_id int, time_stamp TIMESTAMP);
Create table If Not Exists Confirmations (user_id int, time_stamp TIMESTAMP, action confirmation_status);

Truncate table Signups;
insert into Signups (user_id, time_stamp) values ('3', '2020-03-21 10:16:13');
insert into Signups (user_id, time_stamp) values ('7', '2020-01-04 13:57:59');
insert into Signups (user_id, time_stamp) values ('2', '2020-07-29 23:09:44');
insert into Signups (user_id, time_stamp) values ('6', '2020-12-09 10:39:37');

Truncate table Confirmations;
insert into Confirmations (user_id, time_stamp, action) values ('3', '2021-01-06 03:30:46', 'timeout');
insert into Confirmations (user_id, time_stamp, action) values ('3', '2021-07-14 14:00:00', 'timeout');
insert into Confirmations (user_id, time_stamp, action) values ('7', '2021-06-12 11:57:29', 'confirmed');
insert into Confirmations (user_id, time_stamp, action) values ('7', '2021-06-13 12:58:28', 'confirmed');
insert into Confirmations (user_id, time_stamp, action) values ('7', '2021-06-14 13:59:27', 'confirmed');
insert into Confirmations (user_id, time_stamp, action) values ('2', '2021-01-22 00:00:00', 'confirmed');
insert into Confirmations (user_id, time_stamp, action) values ('2', '2021-02-28 23:59:59', 'timeout');

-- SOLUTION 1
SELECT
    s.user_id,
    ROUND(COALESCE(t2.cnt_confirmed::decimal/t1.cnt,0),2) as confirmation_rate
FROM Signups s
LEFT JOIN (
    SELECT s.user_id, COUNT(s.user_id) as cnt
    FROM Signups s
    INNER JOIN Confirmations c ON c.user_id=s.user_id
    GROUP BY s.user_id
) as t1 ON s.user_id=t1.user_id
LEFT JOIN (
    SELECT s.user_id, COUNT(s.user_id) as cnt_confirmed
    FROM Signups s
    INNER JOIN Confirmations c ON c.user_id=s.user_id
    WHERE c.action = 'confirmed'
    GROUP BY s.user_id
) as t2 ON s.user_id=t2.user_id;

-- SOLUTION 2
SELECT
    s.user_id,
    ROUND(COUNT(c.action) FILTER (WHERE c.action = 'confirmed') / COUNT(*)::decimal,2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id;
