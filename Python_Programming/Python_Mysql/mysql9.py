#TRUNCATE (DELETE ALL VALUE)....
import mysql.connector as myconn
mydb=myconn.connect(host="localhost", user="root", password="itzme")
db_cursor=mydb.cursor()
db_deleteAll="truncate table newswarup.students"
db_cursor.execute(db_deleteAll)
mydb.commit()
print("All row deleted")
db_cursor.execute("select * from newswarup.students")
for i in db_cursor.fetchall(): #print all values using loop, but nothing will print here.Because the table is empty.
    print(i) 