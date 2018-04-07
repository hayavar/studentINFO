from tkinter import *
from tkinter import messagebox
import sqlite3
import time

w1 = Tk()
usn = StringVar()
usn.__init__(w1)
name2 = StringVar()
name2.__init__(w1)
gpa = StringVar()
gpa.__init__(w1)
passw = StringVar()
passw.__init__(w1)
sem = StringVar()
sem.__init__(w1)
dept = StringVar()
eff = StringVar()
impy = StringVar()


def login():
    db = sqlite3.connect("STDLOGIN.db")
    c = db.cursor()
    sql = "SELECT * FROM stuff WHERE PASSWORD=?"
    c.execute(sql, [(passw.get())])
    res = c.fetchall()
    if res:

        cer = "SELECT * FROM INF WHERE NAME=? AND PASSWORD=?"
        c.execute(cer, [(name1.get()), (passw.get())])
        row = c.fetchone()
        if row:
            messagebox.showinfo("WELCOME", "RECORD FOUND")
            name2.set(row[0])
            usn.set(row[1])
            sem.set(row[2])
            dept.set(row[3])
            gpa.set(row[4])
            eff.set(row[5])
            impy.set(row[6])
            c.close()
            db.close()
        else:
            messagebox.showerror("ERROR", "Record Not Found.\n"
                                          "Please Input Correct username And Password")
            clear()

    else:
        messagebox.showerror("ERROR", "Record Not Found.\n"
                                      "Please Input Correct username And Password")
        clear()


def clear():
    usn.set('')
    name2.set('')
    sem.set('')
    dept.set('')
    gpa.set('')
    eff.set('')
    impy.set('')
    name1.set('')
    passw.set('')


w1.title("Computer Science Department")
w1.geometry("1000x400")
w1.configure(border=1.0)
w1.configure(background="#F5FFCF")
canvas = Canvas(w1, width=100, height=100, background="GREEN")
canvas.configure(border=0.5)
canvas.place(x=300, y=50)
my_image = PhotoImage(file='C:\\Users\\hp\\Downloads\\kl.png')
canvas.create_image(0, 0, anchor="nw", image=my_image)
ptilte = Label(w1, text="                STUDENT LOGIN           ", bg="#DBE7FF", font=('ARIAL', 12, "bold"),
               fg="PURPLE")
ptilte.winfo_geometry()
ptilte.pack()

name1 = StringVar()
usn1 = StringVar()
gpa1 = StringVar()

l1 = Label(w1, text="USERNAME:", fg="BLUE", font=(None, 10, "bold"), bg="#F5FFCF")
e1 = Entry(w1, textvariable=name1)
l2 = Label(w1, text="PASSWORD:", fg="RED", font=(None, 10, "bold"), bg="#F5FFCF")
e2 = Entry(w1, textvariable=passw, show='*')
l3 = Label(w1, text="NAME:", fg="BLUE", font=(None, 9, "bold"), bg="white")
e3 = Entry(w1, textvariable=name2, fg="RED", bg="white",font=("",10,"bold"))
l4 = Label(w1, text="USN:", fg="BLUE", font=(None, 9, "bold"), bg="white")
e4 = Entry(w1, textvariable=usn, fg="RED",font=("",10,"bold"))
l5 = Label(w1, text="SEM:", fg="GREEN", font=(None, 9, "bold"), bg="white")
e5 = Entry(w1, textvariable=sem, fg="RED",font=("",10,"bold"))
l6 = Label(w1, text="DEPT:", fg="GREEN", font=(None, 9, "bold"), bg="white")
e6 = Entry(w1, textvariable=dept, fg="RED",font=("",10,"bold"))
l7 = Label(w1, text="GPA:", fg="GREEN", font=(None, 9, "bold"), bg="white")
e7 = Entry(w1, textvariable=gpa, fg="RED",font=("",10,"bold"))
l8 = Label(w1, text="EFFNCY(%):", fg="GREEN", font=(None, 10, "bold"), bg="white")
e8 = Entry(w1, textvariable=eff, fg="RED",font=("",10,"bold"))
l9 = Label(w1, text="IMPT_AREA:", fg="GREEN", font=(None, 10, "bold"), bg="white")
e9 = Entry(w1, textvariable=impy, fg="RED",font=("",10,"bold"))

b1 = Button(w1, text="Login", command=login, border=0.5, bg="#8CB2B7", fg="blue", font=(None, 10, "bold"))
b2 = Button(w1, text="Clear", command=clear, border=0.5, bg="#8CB2B7", fg="blue", font=(None, 10, "bold"))
l1.pack()
e1.pack(fill="both")
l2.pack()
e2.pack(fill="both")
l3.pack()
e3.pack(fill="both")
l4.pack()
e4.pack(fill="both")
l5.pack()
e5.pack(fill="both")
l6.pack()
e6.pack(fill="both")
l7.pack()
e7.pack(fill="both")
l8.pack()
e8.pack(fill="both")
l9.pack()
e9.pack(fill="both")

b1.pack()
b2.pack()


def hj():
    l1.place(x=300, y=160)
    e1.place(x=400, y=160)
    l2.place(x=300, y=190)
    e2.place(x=400, y=190)
    l3.place(x=550, y=60)
    e3.place(x=600, y=60)
    l4.place(x=550, y=90)
    e4.place(x=600, y=90)
    l5.place(x=550, y=120)
    e5.place(x=600, y=120)
    l6.place(x=550, y=150)
    e6.place(x=600, y=150)
    l7.place(x=550, y=180)
    e7.place(x=600, y=180)
    l8.place(x=550, y=210)
    e8.place(x=650, y=210)
    l9.place(x=550, y=240)
    e9.place(x=650, y=240)
    b1.place(x=300, y=230)
    b2.place(x=350, y=230)


hj()
w1.mainloop()
time.sleep(2)
