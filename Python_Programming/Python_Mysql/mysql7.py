#UPDATE.....
import mysql.connector as myconn
mydb=myconn.connect(host="localhost", user="root", password="itzme")
db_cursor=mydb.cursor()
db_update="update newswarup.students set S_roll=%s where S_name=%s"
db_value=(101,"Mayank")
db_cursor.execute(db_update, db_value)
mydb.commit()
print(db_cursor.rowcount, "Data Updated....")
db_cursor.execute("select * from newswarup.students")
for i in db_cursor.fetchall(): #print all values using loop
    print(i)