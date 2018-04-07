import sqlite3

conn=sqlite3.connect("student.db")
c=conn.cursor()



def create_table():
    c.execute('CREATE TABLE std(NAME TEXT,USN TEXT, GPA REAL, EFFICIENCY REAL,IMP_AREA TEXT)')

def entry():
    for row in range(3):
        name=input("ente the name")
        usn=input("enter the usn")
        gp=input("enter the gpa")
        eff=input("enter the efficiency")
        imp=input("enter the area student lacks")
        c.execute("INSERT INTO std (NAME,USN,GPA,EFFICIENCY,IMP_AREA) VALUES(?,?,?,?,?)",
                  (name,usn,gp,eff,imp))
        conn.commit()


create_table()
entry()
c.close()
conn.close()