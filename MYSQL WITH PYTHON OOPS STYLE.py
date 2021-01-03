import time
from random import randint
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="kamal@1991",

)
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS kamal2")
cursor.execute("SHOW DATABASES")
#for x  in cursor:
#    print(x)
mydb1 = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="kamal@1991",
    database="kamal2"
)

cursor1 = mydb1.cursor()
cursor1.execute("CREATE TABLE IF NOT EXISTS ems1(current1 INTEGER(10),current2 INTEGER(10),current3 INTEGER(10),user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
#cursor1.execute("CREATE TABLE IF NOT EXISTS ems2(current1 INTEGER(10),current2 INTEGER(10),current3 INTEGER(10),user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
cursor1.execute("SHOW TABLES")
for y in cursor1:
    print(y)

##########################INSERT INTO THE TABLE##############################################################
"""
while True:
    value1=str(randint(50,100))
    value2=str(randint(50,100))
    value3=str(randint(50, 100))

    sql = "INSERT INTO ems1(current1,current2,current3) VALUES(%s,%s,%s)"
    values=(value1,value2,value3)
    cursor1.execute(sql,values)
    mydb1.commit()
    print("1 record inserted, ID:", cursor1.lastrowid)
    time.sleep(1)
"""
####################################### INSERT INTO THE OTHER TABLE ##########################################
"""
while True:
    value1=str(randint(50,100))
    value2=str(randint(50,100))
    value3=str(randint(50, 100))

    sql = "INSERT INTO ems2(current1,current2,current3) VALUES(%s,%s,%s)"
    values=(value1,value2,value3)
    cursor1.execute(sql,values)
    mydb1.commit()
    print("1 record inserted, ID:", cursor1.lastrowid)
    time.sleep(1)
"""
#######################################select from the table###################################################
"""
cursor1.execute("SELECT * FROM ems1")
#cursor1.execute("SELECT current1 FROM ems1")
#mydata = cursor1.fetchall()   # this is used to fetch complete data in columns
mydata = cursor1.fetchall()    # this is used to fetch only one data in columns
for x in mydata:
    print(x)
"""
##################################Select from the table with filter ###############################
"""
cursor1.execute("SELECT * FROM ems1 WHERE current1=23")
mydata = cursor1.fetchall()   # this is used to fetch complete data in columns
#mydata = cursor1.fetchone()    # this is used to fetch only one data in columns
for x in mydata:
    print(x)
"""
##############################order by or sort by  ascending and decending #############################
"""
#cursor1.execute("SELECT * FROM ems1 ORDER BY current1")  # here we can check the data in the ascending oder via current1
cursor1.execute("SELECT * FROM ems1 ORDER BY current1 DESC")
mydata = cursor1.fetchall()   # this is used to fetch complete data in columns
#mydata = cursor1.fetchone()    # this is used to fetch only one data in columns
for x in mydata:
    print(x)
"""
############################Delete the table ####################################################
# sqw = "DELETE FROM ems1 WHERE current1>90"
""""
sqw = "DELETE FROM ems1 WHERE current1 > %s"  # prevent sql injection
value = ("50",)
cursor1.execute(sqw,value)

mydb1.commit()

print(cursor1.rowcount, "record(s) deleted")
"""

################################drop the tables#######################################
"""
sql = "DROP TABLE IF EXISTS ems2"

cursor1.execute(sql)
"""
##############################update the tables######################################
"""
sql = "UPDATE ems1 SET current1 = 23 WHERE current1>85 "
cursor1.execute(sql)
mydb1.commit()
print(cursor1.rowcount, "record(s) affected")
"""
############################limit the table###############################################
cursor1.execute("SELECT * FROM ems1 LIMIT 5")

myresult = cursor1.fetchall()

for x in myresult:
  print(x)