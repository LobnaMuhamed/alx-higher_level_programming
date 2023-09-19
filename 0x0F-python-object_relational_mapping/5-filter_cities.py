#!/usr/bin/python3

"""
a script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cr = db.cursor()
    state_name = sys.argv[4]

    cr.execute("SELECT cities.name FROM cities "
                "INNER JOIN states ON states.id=cities.state_id "
                "WHERE states.name=%s ORDER BY cities.id ASC", (state_name, ))

    rows = cr.fetchall()
    
    data_list = list(row[0] for row in rows)
    print(*data_list, sep=", ")
    cr.close()
    db.close()
