#!/usr/bin/python3

"""
Module: 0-select_states
Lists all states fro the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
states = cursor.fetchall()
for state in states:
    print(state)

cursor.close()
db.close()
