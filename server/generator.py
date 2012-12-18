import MySQLdb 
import sys

def main():
    db = None

    try:
        db = MySQLdb.connect(host="localhost", user="vuvuzela", passwd="alezuvuv", db="freeside")
        db.query("select version()");
        result = db.use_result()
        print result.fetch_row()[0]
    except mysql.Error, e:        
        sys.exit(1)
    finally:
        if db:
            db.close()

def printzones():
    db = None

    try:
        db = MySQLdb.connect(host="localhost", user="vuvuzela", passwd="alezuvuv", db="freeside")
        cur = db.cursor()
        cur.execute("SELECT name, description FROM zone")
        for row in cur.fetchall():
            name = str(row[0])
            description = str(row[1])
            print name + ": " + description
            
    except mysql.Error, e:        
        sys.exit(1)
    finally:
        if db:
            db.close()


if __name__=='__main__':
    main()
    printzones()
