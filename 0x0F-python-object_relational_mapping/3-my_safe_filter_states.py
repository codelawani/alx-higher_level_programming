#!/usr/bin/python3
from sys import argv as av
import MySQLdb

"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument.
This script should take 3 arguments:
mysql username, mysql password,
database name and state name searched
"""
st_name = av[4]
db = MySQLdb.connect("localhost", *av[1:4], 3306)
cursor = db.cursor()
cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY states.id",(st_name,))
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
db.close()
