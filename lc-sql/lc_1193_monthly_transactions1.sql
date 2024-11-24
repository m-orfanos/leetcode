-- SCHEMA
-- CREATE TYPE transaction_state AS enum('approved', 'declined');
Create table If Not Exists Transactions (id int, country varchar(4), state transaction_state, amount int, trans_date TIMESTAMP);
Truncate table Transactions;
insert into Transactions (id, country, state, amount, trans_date) values ('121', 'US', 'approved', '1000', '2018-12-18');
insert into Transactions (id, country, state, amount, trans_date) values ('122', 'US', 'declined', '2000', '2018-12-19');
insert into Transactions (id, country, state, amount, trans_date) values ('123', 'US', 'approved', '2000', '2019-01-01');
insert into Transactions (id, country, state, amount, trans_date) values ('124', 'DE', 'approved', '2000', '2019-01-07');

-- SOLUTION
SELECT
    TO_CHAR(t.trans_date, 'YYYY-MM') as month,
    t.country,
    COUNT(*) as trans_count,
    COUNT(*) FILTER (WHERE t.state = 'approved') as approved_count,
    SUM(t.amount) as trans_total_amount,
    COALESCE(SUM(t.amount) FILTER (WHERE t.state = 'approved'),0) as approved_total_amount
FROM Transactions t
GROUP BY month, t.country;
