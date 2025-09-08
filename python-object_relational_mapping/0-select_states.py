#!/usr/bin/python3

"""
This module lists all states from the database hbtn_0e_0_usa.
It connects to a MySQL server and retrieves all states ordered by id.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    # Create cursor object
    cursor = db.cursor()
    
    # Execute SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all results
    states = cursor.fetchall()
    
    # Display results
    for state in states:
        print(state)
    
    # Close cursor and database connection
    cursor.close()
    db.close()
