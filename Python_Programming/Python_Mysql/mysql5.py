import mysql.connector as myconn
mydb=myconn.connect(host="localhost", user="root", password="itzme", database="Newswarup")
print(mydb, "Connection Successful....")
db_cursor=mydb.cursor()
# db_cursor.execute("insert into Students(S_name, S_roll) values(%s, %s)", ("Jubaraj", 51))
db_insert="insert into Students(S_name, S_roll) values(%s, %s)" #insert value in one line
db_list=[("Mayank", 100), ("Hemant", 115), ("Pranit", 26)]      #(-----------"------------)
db_cursor.executemany(db_insert, db_list)                       #(-----------"------------)
mydb.commit()
print(db_cursor.rowcount, "Record Inserted..")

