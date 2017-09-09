#      As a:   Snapper 
# I WANT TO:   Send a snap to someone who has most frequently sent me snaps
#   So that:   We can keep in touch

# find a person that has snapchatted 'yamz' the most
# send one to that person

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
    show_snaps = '''
                SELECT *
                    FROM Snaps
    '''
    show_private_snaps = '''
                    SELECT *
                        FROM Private_Snaps
    '''
    print("*************Snaps table*************")
    cmd = cur.mogrify(show_snaps)
  
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    print()
    print("*************Private_Snaps table*************")
    cmd = cur.mogrify(show_private_snaps)
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)


def main():     
    db, user, password = 'snapchat', 'isdb16', 'sbhotika'
    conn = psycopg2.connect(database=db, user=user, password=password)
    conn.autocommit = True
    cur = conn.cursor()

    username = 'yamz'
    snap_id = 11
    date_sent = '11/7/2016'
    seconds = 5

    tmp1 = '''
            SELECT u.username, count(p.snap_id) as count
                FROM Snappers as u
                INNER JOIN Snaps as s
                    ON s.username = u.username
                INNER JOIN Private_Snaps as p
                    ON (p.snap_id = s.snap_id and s.username != 'yamz')
                WHERE (p.to_username = 'yamz' OR s.username = 'yamz')
                GROUP BY u.username
                ORDER BY count DESC;
    '''
    
    tmp2 = '''
            INSERT INTO Snaps(snap_id, username, date_sent, seconds)
            VALUES (%s, %s, %s, %s)
    '''
    
    tmp3 = '''
            INSERT INTO Private_Snaps(to_username, snap_id)
            VALUES (%s, %s)
    '''

    print_tables(cur, True)

    # cmd1 gets the list of users who have snapchatted 'yamz' the most
    cmd1 = cur.mogrify(tmp1)
    print_cmd(cmd1)
    cur.execute(cmd1)
    rows = cur.fetchall()

    # select the person at the top of list
    (to_username, count) = rows[0]

    # create a snap
    cmd2 = cur.mogrify(tmp2, (snap_id, to_username, date_sent, seconds))
    print_cmd(cmd2)
    cur.execute(cmd2)

    # create private snap
    cmd3 = cur.mogrify(tmp3, (username, snap_id))
    print_cmd(cmd3)
    cur.execute(cmd3)

    print_tables(cur, False)

main()