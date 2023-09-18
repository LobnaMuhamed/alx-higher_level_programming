#!/usr/bin/python3

"""
a script that lists all states with a name starting with N
"""

import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cr = db.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE 'N%'")

    rows = cr.fetchall()

    for row in rows:
        print(row)

    cr.close()
    db.close()
