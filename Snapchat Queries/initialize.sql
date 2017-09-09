\c postgres
DROP DATABASE IF EXISTS snapchat;

CREATE database snapchat;
\c snapchat

\i create.SQL

\copy Users(user_id) 									FROM 'users.csv' 			csv header
\copy Businesses(business_id, name) 					FROM 'businesses.csv' 		csv header
\copy Orders(order_id, business_id, date_placed) 		FROM 'orders.csv' 			csv header
\copy Advertisements(ad_id, order_id, cost, num_views) 	FROM 'advertisements.csv' 	csv header
\copy Snappers(username, name, location, snapscore) 	FROM 'snappers.csv' 		csv header
\copy Snaps(snap_id, username, date_sent, seconds) 		FROM 'snaps.csv' 			csv header
\copy Story(story_id, snap_id, num_views) 				FROM 'story.csv' 			csv header
\copy Private_Snaps(to_username, snap_id) 				FROM 'private_snaps.csv' 	csv header
-- ============================================================
  
