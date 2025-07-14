#!/usr/bin/python3
"""
Script that displays all values in the states table where name matches the argument
Safe from MySQL injections
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))
    results = cursor.fetchall()
    
    for row in results:
        print(row)
    
    cursor.close()
    db.close()
