import mysql.connector as myconn
mydb=myconn.connect(host="localhost", user="root", password="itzme")
db_cursor=mydb.cursor()
db_cursor.execute("select * from newswarup.students")
# db_select=db_cursor.fetchall() #to see all value in a table
# db_select1=db_cursor.fetchone()...To see one value
# print(db_select1)
for i in db_cursor.fetchall(): #print all values using loop
    print(i)