SET client_min_messages TO WARNING;

-- SCHEMA
Create table If Not Exists Tweets(tweet_id int, content varchar(50));
Truncate table Tweets;
insert into Tweets (tweet_id, content) values ('1', 'Let us Code');
insert into Tweets (tweet_id, content) values ('2', 'More than fifteen chars are here!');

-- SOLUTION
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;
