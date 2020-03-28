#!/usr/bin/python3
"""
Lists all states with a name starting ith N
"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE states.name LIKE 'N%'\
            ORDER BY states.id ASC"
            )
    query = cursor.fetchall()
    for row in query:
        print(row)
    cursor.close()
    db.close()
