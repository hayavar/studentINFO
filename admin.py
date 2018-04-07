import sqlite3


conn=sqlite3.connect("ADMIN.db")
c=conn.cursor()
def create():
    c.execute("CREATE TABLE stuff(NAME TEXT,USN TEXT,SEMISTER REAL,DEPARTMENT TEXT,GPA REAL,EFFICIENCY REAL,IMP_AREA TEXT)")
def entry():
    for row in range(3):
        user=input("enter the username")
        passw=input("enter the password")
        c.execute("INSERT INTO stuff(USERNAME,PASSWORD) VALUES(?,?)",(user,passw))
        conn.commit()
def entry1():
    for row in range(3):
        name=input("enter the name")
        usn=input("enter the usn")
        sem=input("enter the semister")
        dept=input("enter the department")
        gpa=input("enter the gpa")
        eff=input("enter the efficiency")
        imp=input("enter the area in which student lacks")
        c.execute("INSERT INTO INF(NAME,USN,SEMISTER,DEPARTMENT,GPA,EFFICIENCY,IMP_AREA) VALUES(?,?,?,?,?,?,?)",(name,usn,sem,dept,gpa,eff,imp))
        conn.commit()


create()
#entry()

#entry1()
c.close()
conn.close()
