#!/usr/bin/python3

"""
    Module: 5-filter_cities
    Lists all cities in a given state
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

    my_query = "SELECT c.name \
     FROM cities c INNER JOIN states s \
     ON s.id = c.state_id \
    WHERE s.name = %s ORDER BY c.id ASC"
    my_cursor.execute(my_query, (state_name,))

    rows = my_cursor.fetchall()
    print(", ".join([row[0] for row in rows]))

    my_cursor.close()
    db.close()
