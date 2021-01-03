import time
from random import randint
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="kamal@1991",
    database="kamal1",
)
sql_cursor = mydb.cursor()
#sql_cursor.execute("CREATE DATABASE KAMAL1")
#sql_cursor.execute("SHOW DATABASES")
#for db in sql_cursor:
#    print(db)

#sql_cursor.execute("CREATE TABLE EMS(current INTEGER(10),current1 INTEGER(10),current2 INTEGER(10),user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
sql_cursor.execute("SHOW TABLES")
for table in sql_cursor:
    print(table[0])
while True:
    value1 = str(randint(1,100))
    value2 = str(randint(1, 100))
    value3 = str(randint(1, 100))


    query = "INSERT INTO ems(current,current1,current2) VALUES(%s,%s,%s)"
    values = (value1,value2,value3);
    sql_cursor.execute(query,values)
    mydb.commit()
    print(sql_cursor.rowcount,"record_inserted")
    time.sleep(1)