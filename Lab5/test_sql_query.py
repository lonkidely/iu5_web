import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="123456789",
    db="lab5_db"
)

curs = db.cursor()
curs.execute("insert into Operator (name, count_cycles) values(%s, %s);", ('-', '170'))
db.commit()
curs.close()
db.close()
