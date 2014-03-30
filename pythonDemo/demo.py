import MySQLdb

db = MySQLdb.connect(user='root', db='world', passwd='sglyqfh', host='localhost')


cursor = db.cursor()
cursor.execute("select * from city")
names = [row[1] for row in cursor.fetchall()]
db.close()


print names

