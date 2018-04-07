from tkinter import *
from tkinter import messagebox
import sqlite3
import time

w1 = Tk()
usn = StringVar()
usn.__init__(w1)
name = StringVar()
name.__init__(w1)
gpa = StringVar()
gpa.__init__(w1)
passw = StringVar()
passw.__init__(w1)


def login():
    db = sqlite3.connect("STDLOGIN.db")
    c = db.cursor()
    sql = "SELECT * FROM stuff WHERE PASSWORD=?"
    c.execute(sql, [(passw.get())])
    res = c.fetchall()
    if res:

        messagebox.showinfo("WELCOME", "RECORD FOUND")
        cer = "SELECT * FROM INF"
        c.execute(cer)
        row = c.fetchone()
        name.set(row[0])
        usn.set(row[1])
        gpa.set(row[4])
        c.close()
        db.close()

    else:
        messagebox.showerror("ERROR", "RECORD NOT FOUND")
        clear()


def clear():
    usn.set('')
    name.set('')
    gpa.set('')
    name1.set('')
    passw.set('')


w1.title("Student Login")

w1.geometry("500x300")

w1.configure(background="#8CB2B7")

ptilte = Label(w1, text="                student login            ")
ptilte.winfo_geometry()
ptilte.pack()

name1 = StringVar()
usn1 = StringVar()
gpa1 = StringVar()

l1 = Label(w1, text="USERNAME",fg="BLUE")
e1 = Entry(w1, textvariable=name1)
l2 = Label(w1, text="PASSWORD",fg="RED")
e2 = Entry(w1, textvariable=passw, show='*')
l3 = Label(w1, text="NAME",fg="BLUE")
e3 = Entry(w1, textvariable=name)
l4 = Label(w1, text="USN",fg="RED")
e4 = Entry(w1, textvariable=usn)
l5 = Label(w1, text="GPA", font='Arial',fg="GREEN")
e5 = Entry(w1, textvariable=gpa)

b1 = Button(w1, text="login", command=login)
b2 = Button(w1, text="clear", command=clear)
l1.pack()
e1.pack()
l2.pack()
e2.pack()
l3.pack()
e3.pack()
l4.pack()
e4.pack()
l5.pack()
e5.pack()
b1.pack()
b2.pack()
l1.place(x=10, y=40)
e1.place(x=100, y=40)
l2.place(x=10, y=70)
e2.place(x=100, y=70)
l3.place(x=10, y=100)
e3.place(x=100, y=100)
l4.place(x=10, y=130)
e4.place(x=100, y=130)
l5.place(x=10, y=160)
e5.place_configure(x=100,y=160)
b1.place(x=10, y=190)
b2.place(x=50, y=190)
w1.mainloop()
time.sleep(2)
