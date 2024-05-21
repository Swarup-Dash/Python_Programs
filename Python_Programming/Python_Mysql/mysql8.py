# DELETE......
import mysql.connector as myconn
mydb=myconn.connect(host="localhost", user="root", password="itzme")
db_cursor=mydb.cursor()
db_delete="delete from newswarup.students where S_name=%s" 
db_value=("pranit",)
db_cursor.execute(db_delete, db_value)
mydb.commit()
print(db_cursor.rowcount, "row deleted")
db_cursor.execute("select * from newswarup.students")
for i in db_cursor.fetchall(): #print all values using loop
    print(i)