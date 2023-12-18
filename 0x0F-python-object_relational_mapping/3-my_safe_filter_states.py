#!/usr/bin/python3

"""
Displays all values in the states table of the database
hbtn_0e_0_usa, where name matches the argument.
script should take 4 arguments: mysql username, mysql
password, database name and state name searched.
safe from MySQL injections!
List must be sorted in ascending order by states.id
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                   (argv[4],))
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    db.close()
