import sqlite3
import time



username=input("enter username")
password=input("enter password")
with sqlite3.connect("student.db") as c:
    cur=c.cursor()
fetch=("SELECT * FROM std  where NAME=? AND USN=?")
cur.execute(fetch,[(username),(password)])
result=cur.fetchall()
if result:
    print("login successfull")
    time.sleep(2)
    for rown in result:
        print("NAME=",rown[0])
        print("USN=",rown[1])
        print("GPA=",rown[2])
        print("EFFICIENCY=",rown[3],"%")
        print("IMPROVEMENT AREA=",rown[4])
        break
else:
    print("ACCESS DENIED")
    exit()