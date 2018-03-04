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

namedict = ({"first_name":"Joshua", "last_name":"Drake"},
            {"first_name":"Steven", "last_name":"Foo"},
            {"first_name":"David", "last_name":"Bar"})

try:
    # create a psycopg2 cursor that can execute queries
    cursr = conn.cursor()
    # create a new table with a column called "name" IF NOT EXISTS  
    cursr.execute("""CREATE TABLE IF NOT EXISTS tutorials (first_name char(40), last_name char(40))""")
    cursr.executemany("""INSERT INTO tutorials (first_name,last_name) VALUES (%(first_name)s, %(last_name)s)""", namedict)
    # run a SELECT statement   
    cursr.execute("""SELECT * from tutorials""")
    rows = cursr.fetchall()
    print(rows) 
    conn.commit()
    cursr.close()
    conn.close()
except Exception as e:
    print(">>>*** Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)
