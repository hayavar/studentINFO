import sqlite3
import time
conn=sqlite3.connect("login1.db")
c=conn.cursor()
def create():
    c.execute("CREATE TABLE STDLOGIN(USERNAME TEXT,PASSWORD TEXT)")
def entry():
    for row in range(3):
        user=input("enter the username")
        passw=input("enter the password")
        c.execute("INSERT INTO STDLOGIN(USERNAME,PASSWORD) VALUES(?,?)",(user,passw))
        conn.commit()


create()
entry()
c.close()
conn.close()
