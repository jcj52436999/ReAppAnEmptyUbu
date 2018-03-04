#/usr/bin/python3
#
#

# saveArrayToPostgreSQLTable.py

import psycopg2
# try to connect
connect_str = "dbname='reappanemptyubu' user='jcj52436999' host='localhost' " + "password='STL2lmnm'"
try:
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
except Exception as e:
    print(">>>*** ReAppAnEmptyUbu is UNABLE TO CONNECT TO THE DATABASE. Invalid dbname, user or password?")
    print(e)

try:
    # create a psycopg2 cursor that can execute queries
    cursr = conn.cursor()
    # create a new table with a single column called "name"
    # cursor.execute("""CREATE TABLE tutorials (name char(40));""")
    # run a SELECT statement - no data in there, but we can try it
    cursr.execute("""SELECT * FROM tutorials""")
    rows = cursr.fetchall()
    print(rows)
except Exception as e:
    print(">>>*** Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)
