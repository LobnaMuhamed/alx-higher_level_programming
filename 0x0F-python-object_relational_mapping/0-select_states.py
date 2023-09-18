#!/usr/bin/python3

"""
a script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ = '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, username=sys.argv[1],
            password=sys.argv[2], db=sys.argv[3])

    cr = db.cursor()
    cr.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cr.feachall()

    for row in rows:
        print(row)

    cr.close()
    db.close()
