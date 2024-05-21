import mysql.connector as myconn
mydb=myconn.connect(host="localhost", user="root", password="itzme", database="Newswarup")
print(mydb, "Connection Successful....")
db_cursor=mydb.cursor()
db_cursor.execute("create table Employee2(S_name varchar(20), S_roll int)")
print("Table created..")
db_cursor.execute("show tables")
for i in db_cursor:
    print(i)
