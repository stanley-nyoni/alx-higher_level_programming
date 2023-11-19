#!/usr/bin/python3

"""
    Module: 1-filter_states
    Lists all states with name starting with N
"""


import sys
import MySQLdb


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
    my_query = "SELECT * FROM states WHERE name LIKE BINARY \
    'N%' ORDER BY states.id ASC;"
    my_cursor.execute(my_query)

    states = my_cursor.fetchall()
    for state in states:
        print(state)

    my_cursor.close()
    db.close()
