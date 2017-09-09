#      As a:   Snapchat internal executive 
# I WANT TO:   See how much my business clients are spending on each advertisement
#   So that:   I can understand cash inflow of my company

import psycopg2
import sys
import pprint

SHOW_CMD = True
def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

def main(): 	
	db, user, password = 'snapchat', 'isdb16', 'sbhotika'
	conn = psycopg2.connect(database=db, user=user, password=password)
	conn.autocommit = True
	cur = conn.cursor()

#First query joins the businesses and orders tables
#This way, the business is matched up with its respective orders
	tmp1 = '''
			SELECT Businesses.business_id
				FROM Businesses
				INNER JOIN Orders
					ON Orders.business_id = Businesses.business_id;
	'''
#Second query adds the total revenue from each ad
#Revenue is determined by the cost of the ad, multiplied by the number of views	
	tmp2 = ''' 
			SELECT SUM(a.cost * a.num_views)
				FROM Advertisements as a
					INNER JOIN Orders
						ON Orders.order_id = a.order_id
					WHERE (Orders.business_id ILIKE %s);
	'''
	cmd1 = cur.mogrify(tmp1)  
	print_cmd(cmd1)
	cur.execute(cmd1)
	
	rows = cur.fetchall()
	print("Business                Total cost ")
	for row in rows:
		(uid,) = row
		cmd2 = cur.mogrify(tmp2, ('%'+uid+'%',))
		cur.execute(cmd2)
		rows = cur.fetchall()
		(total_cost,) = rows[0]
		print("%s              %d" % (uid, total_cost))

main()