#!/usr/bin/python3

"""
Module: 2-my_filter_states
Takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
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
        user=username,
        passwd=password,
        db=database)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                WHERE name = '{}' ORDER BY id".format(state_name))

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
