#!/usr/bin/python3

"""
    Module: 4-cities_by_state
    Lists all cities from the database
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    my_cursor = db.cursor()
    my_cursor.execute("SELECT cities.id, cities.name, states.name \
                      FROM cities JOIN states \
                      ON states.id = cities.state_id \
                      ORDER BY cities.id ASC")

    rows = my_cursor.fetchall()
    for row in rows:
        print(row)
