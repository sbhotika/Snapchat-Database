-- simple_queries.sql
-- needs to be connected to the Snapchat database
\c snapchat

-- User story e
\echo **********(E) Showing all Snapchat Users ***********
\echo **********Showing Businesses ***********
SELECT b.name
FROM Businesses as b 
INNER JOIN Users as u 
ON u.user_id  = b.business_id;

\echo **********Showing Snappers ***********
SELECT s.name
FROM Snappers as s 
INNER JOIN Users as u 
ON u.user_id  = s.username;
---------
------ User story f
\echo **********(F) Showing total advertising cost for a given business_id ('frat id')***********
SELECT SUM(a.cost * a.num_views) AS cost
FROM Advertisements as a
INNER JOIN Orders as o 
ON o.order_id = a.order_id
WHERE o.business_id = 'frat bro';
-------
------ User story g
\echo **********(G) Showing total revenue for Snapchat internal executive ***********
SELECT SUM(a.cost * a.num_views) AS cost
FROM Advertisements as a
INNER JOIN Orders as o 
ON o.order_id = a.order_id;
--------
--User story h
\echo **********(H) Showing the snapscore of a given username ('tikka') ***********
SELECT snapscore
FROM Snappers
WHERE username = 'tikka';
------
------ User story i
\echo **********(I) Showing the average duration of Snaps*********** 
SELECT avg(s.seconds)
FROM Snaps as s;
------
---- User story j
\echo **********(J) Showing location and number of Snappers in that location***********
SELECT s.location, count(s.username)
FROM Snappers as s
GROUP BY s.location;
