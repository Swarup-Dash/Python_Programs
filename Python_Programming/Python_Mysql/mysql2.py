import mysql.connector as myconn
mydb=myconn.connect(host="localhost", user="root", password="itzme")
print(mydb, "Connection Successful....")