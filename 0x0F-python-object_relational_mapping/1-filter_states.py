#!/usr/bin/python3
from sys import argv as av
import MySQLdb

"""
lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa
This script should take 3 arguments:
mysql username, mysql password and database name
"""

db = MySQLdb.connect("localhost", *av[1:])
cursor = db.cursor()
cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
db.close()
