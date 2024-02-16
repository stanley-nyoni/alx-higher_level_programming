#!/usr/bin/python3

"""
Module: 1-filter_states
Lists all states that starts with 'N' from the database hbtn_0e_0_usa
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
        database=database
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states \
                   WHERE name LIKE 'N%' ORDER BY states.id ASC")
    rows = cursor.fetchall()

    for state in rows:
        print(state)

    cursor.close()
    db.close()
