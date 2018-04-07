import sqlite3


conn=sqlite3.connect("stdadmin.db")
c=conn.cursor()
def create():
    c.execute("CREATE TABLE stuff(NAME TEXT,USN TEXT,SEMISTER REAL,DEPARTMENT TEXT,GPA REAL,EFFICIENCY REAL,IMP_AREA TEXT)")



create()