#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM states, cities WHERE cities.state_id = states.id ORDER BY cities.id")
    cts = cur.fetchall()
    for ct in cts:
        print (ct)
    cur.close()
    db.close()
