#!/usr/bin/python3
"""
a script that lists all cities from
the database hbtn_0e_0_usa
This script should take 3 arguments:
mysql username, mysql password and database name
and state name
"""

from sys import argv as av
import MySQLdb

if __name__ == '__main__':
    """Driver code"""
    db = MySQLdb.connect("localhost", *av[1:4], 3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities\
 JOIN states ON cities.state_id = states.id \
WHERE states.name = %s ORDER BY cities.id", (av[4],))
    cities = [row[0] for row in cursor.fetchall()]
    print(", ".join(cities))
    cursor.close()
    db.close()
