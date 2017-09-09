\c snapchat

\echo **********Showing all User IDs of Businesses & Snappers where user_id is a uniquely identifying name***********
SELECT *
FROM Users;

\echo **********Showing all Business IDs & Business Names ***********
SELECT *
FROM Businesses;

\echo **********Showing all Orders of Businesses***********
SELECT *
FROM Orders;

\echo **********Showing all Advertisements Included Per Order ***********
SELECT *
FROM Advertisements;

\echo **********Showing all Snappers & Their Usernames ***********
SELECT *
FROM Snappers;

\echo **********Showing all Snaps Sent between Snappers***********
SELECT *
FROM Snaps;

\echo **********Showing all Stories Posted by Snappers***********
SELECT *
FROM Story;

\echo **********Showing all Private_Snaps between Snappers***********
SELECT *
FROM Private_Snaps;