-- SCHEMA
Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int);
Truncate table Activity;
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5');
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-02', '6');
insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5');

-- SOLUTION
SELECT ROUND(
        1.* COUNT(*) /(
            SELECT COUNT(DISTINCT player_id)
            FROM activity
        ),
        2
    ) as fraction
FROM activity
WHERE (player_id, event_date) IN (
        SELECT
            player_id,
            MIN(event_date) + 1
        FROM activity
        GROUP BY player_id
    );