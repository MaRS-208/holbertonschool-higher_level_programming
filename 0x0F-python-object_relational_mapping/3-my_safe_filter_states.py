#!/usr/bin/python3
"""Write a script that takes in an argument and displays all\
values in the states table of hbtn_0e_0_usa where name matches\
the argument, that is safe from MySQL injections"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE states.name\
    = %(username)s ORDER BY states.id", {'username': argv[4]})
    sts = cur.fetchall()
    for st in sts:
        print(st)
    cur.close()
    db.close()
