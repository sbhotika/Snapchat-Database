#      As a:   Snapper
# I WANT TO:   See who I have exchanged snaps with
#   So that:   I can see who my friends are

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

#Select all the people an individual snapper ('chobani') has sent snaps to
	tmp1 = ''' 
			SELECT Private_Snaps.to_username 
				FROM Private_Snaps
				INNER JOIN Snaps
					ON (Private_Snaps.snap_id = Snaps.snap_id)
				WHERE Snaps.username = 'chobani';
	'''
#Select all the snappers who sent a snapchat to a snapper ('chobani')
	tmp2 = '''
			SELECT distinct(Snappers.username)
				FROM Snappers
				INNER JOIN Snaps
					ON Snaps.username = Snappers.username
				INNER JOIN Private_Snaps
					ON Snaps.snap_id = Private_Snaps.snap_id
				WHERE Private_Snaps.to_username = 'chobani';
	'''

	cmd1 = cur.mogrify(tmp1) 
	cmd2 = cur.mogrify(tmp2) 
	print_cmd(cmd1)
	cur.execute(cmd1)
	
	rows = cur.fetchall()
	print()
	for row in rows:
		uid_1 = row
		print("%s" % (uid_1))

	print_cmd(cmd2)
	cur.execute(cmd2)
	rows = cur.fetchall()
	print("The people that username:chobani has exchanged snapchats with: ")
	for row in rows:
		uid_2 = row
		print("%s" % (uid_2))

main()