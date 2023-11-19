#!/usr/bin/python3

"""
    Module: 3-my_safe_filter_states
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
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id"
    my_cursor.execute(query, (state_name,))

    states = my_cursor.fetchall()
    for state in states:
        if state[1] == state_name:
            print(state)

    my_cursor.close()
    db.close()
