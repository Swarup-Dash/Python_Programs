import mysql.connector as myconn
mydb=myconn.connect(host="localhost", user="root", password="itzme")
print(mydb, "Connection Successful....")
db_cursor=mydb.cursor()
db_cursor.execute("create database Newswarup")
print("database created..")