#!/usr/bin/python3
"""
Cities by states
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cursor = db.cursor()
    cursor.execute('SELECT cities.name FROM cities\
            INNER JOIN states\
            ON cities.state_id=states.id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC', (sys.argv[4],))
    query = cursor.fetchall()
    if len(query) == 0:
        print("")
    for i in range(len(query)):
        if i != len(query) - 1:
            print(query[i][0], end=", ")
        else:
            print(query[i][0])
    cursor.close()
    db.close()
