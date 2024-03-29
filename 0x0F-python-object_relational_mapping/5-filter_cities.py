#!/usr/bin/python3
"""Write a script that takes in the name of a state as an argument and\
lists all cities of that state, using the database hbtn_0e_4_usa"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    q = "SELECT cities.name\
        FROM cities\
        JOIN states ON cities.state_id = states.id\
        WHERE states.name = %(state)s\
        ORDER BY cities.id"
    cur.execute(q, {'state': argv[4]})
    cts = cur.fetchall()
    print(", ".join(ct[0] for ct in cts))
    cur.close()
    db.close()
