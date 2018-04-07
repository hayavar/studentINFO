import sqlite3
import time


username=input("username")
passw=input("password")
with sqlite3.connect("STDLOGIN.db") as db:
    cur=db.cursor()
fetch=("SELECT * FROM stuff WHERE USERNAME=? AND PASSWORD=?")
cur.execute(fetch,[(username),(passw)])
result=cur.fetchall()
if result:
    print("LOGIN SUCCESSFULL")
    time.sleep(1)
    c=("SELECT * FROM INF WHERE NAME=?")
    cur.execute(c,[(username)])
    row=cur.fetchall()
    for row1 in row:
        print("NAME=", row1[0])
        print("USN=", row1[1])
        print("SEMISTER=", row1[2])
        print("DEPEARTMENT=", row1[3],)
        print("GPA=", row1[4])
        print("EFFICIENCY=",row1[5],"%")
        print("IMPROVEMENT AREA=",row1[6])
        break
else:
    print("ACCESS DENIED")
