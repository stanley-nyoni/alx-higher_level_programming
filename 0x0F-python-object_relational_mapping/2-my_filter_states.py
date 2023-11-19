#!/usr/bin/python3

"""
    Module: 2-my_filter_states
    Lists all states matching the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    my_cursor = db.cursor()
    my_cursor.execute("SELECT * FROM states WHERE name LIKE \
                      BINARY %s ORDER BY id", (state_name,))

    states = my_cursor.fetchall()
    for state in states:
        print(state)

    my_cursor.close()
    db.close()
