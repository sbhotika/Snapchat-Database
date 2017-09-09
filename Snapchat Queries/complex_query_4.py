#      As a:   Business  
# I WANT TO:   place an advertising order with Snapchat after A/B testing
#   So that:   users can be better exposed to my business

import psycopg2
import sys
import pprint

SHOW_CMD = True
def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))


def print_tables(cur, first_time):
    if first_time:
        print("OUR ORIGINAL TABLES")
    else:
        print("OUR UPDATED TABLES")
    show_ad = '''
                SELECT *
                    FROM Advertisements
    '''
    show_orders = '''
                    SELECT *
                        FROM Orders
    '''
    print("*************Advertisements table*************")
    cmd = cur.mogrify(show_ad)
  
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    print()
    print("*************Orders table*************")
    cmd = cur.mogrify(show_orders)
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)


def main():     
    db, user, password = 'snapchat', 'isdb16', 'sbhotika'
    conn = psycopg2.connect(database=db, user=user, password=password)
    conn.autocommit = True
    cur = conn.cursor()

    # hard-coded values for this query
    order_id = 6
    business_id = "basic psl"
    date_placed = '12/7/16'

#Find the most successful ad (which got the most views) for a business's order
    tmp1 = '''
            SELECT a.ad_id, a.cost
              FROM Advertisements as a
              JOIN Orders as o 
                ON o.order_id = a.order_id
              WHERE o.business_id = 'basic psl' and a.num_views = (SELECT max (a1.num_views)
                                                                        FROM Advertisements as a1
                                                                        JOIN Orders as o1
                                                                        ON o1.order_id = a1.order_id
                                                                    WHERE o1.business_id = 'basic psl');
    '''

#Place a new order    
    tmp2 = ''' 
            INSERT INTO Orders(order_id, business_id, date_placed)
            VALUES (%s, %s, %s)
    '''
#Put the desired advertisement into the order
    tmp3 = ''' 
            INSERT INTO Advertisements(ad_id, order_id, cost, num_views)
            VALUES (%s, %s, %s, %s)
    '''
    
    # cmd1 gets our most popular ad for a company
    cmd1 = cur.mogrify(tmp1)
    print_cmd(cmd1)
    cur.execute(cmd1)
    rows1 = cur.fetchall()

    print_tables(cur, True) # printing original Orders and Advertisements tables

    #  place a new order with cmd2 -> which does not return anything
    cmd2 = cur.mogrify(tmp2,(order_id, business_id, date_placed))  
    print_cmd(cmd2)
    cur.execute(cmd2)
    
    (ad_id, ad_cost) = rows1[0] # gets first ad with max views
    ad_id += 3 # hard-coded

    # business places order for same advertisement (different order from first)
    cmd3 = cur.mogrify(tmp3,(ad_id, order_id, ad_cost, 1500000))  
    print_cmd(cmd3)
    cur.execute(cmd3)

    print_tables(cur, False) # printing updated Orders and Advertisements tables
  
main()