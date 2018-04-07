from tkinter import *
from tkinter import messagebox
import sqlite3

class window:
    def __init__(self, master):
        self.master = master
        canvas2 = Canvas(self.master, width=150, height=150, border=0.5, bg="navyblue", relief="groove", bd=5)
        canvas2.configure(border=0.5)
        canvas2.place(x=20, y=75)
        self.master.my_image = PhotoImage(file='C:\\Users\\hp\\Documents\\pic1.png')
        canvas2.create_image(0, 0, anchor="nw", image=self.master.my_image)

        self.uname = StringVar()
        self.passw3 = StringVar()
        self.ptilte = Label(self.master, text="             ADMIN LOGIN           ", bg="#DBE7FF",
                            font=('Imprint MT Shadow', 13, "bold"),
                            fg="navyblue", relief="groove")
        Label(self.master, text="Department Of Computer Science & Engineering", font=('Imprint MT Shadow ', 16, "bold"),
              fg="maroon", bg="darkgrey").place(x=70, y=30)
        self.ptilte.pack()
        la1 = Label(self.master, text="USERNAME:", fg="white", font=("", 14, "bold"), bg="darkgrey")

        e1 = Entry(self.master, textvariable=self.uname, fg="navyblue", font=("", 11, "bold"), relief="sunken", bd=5,
                   bg="#F4FCE3")

        lb1 = Label(self.master, text="PASSWORD: ", fg="RED", font=("", 14, "bold"), bg="darkgrey")

        e2 = Entry(self.master, textvariable=self.passw3, show="*", fg="navyblue", font=("", 11, "bold"),
                   relief="sunken", bd=5, bg="#F4FCE3")
        b1 = Button(self.master, text="LOGIN", command=self.login1, font=("ARIAL", 11, "bold"), bg="#555555",
                    fg="white",
                    relief="raised", bd=5)
        b1.pack()
        br = Button(self.master, text="CLEAR", command=self.clear, font=("ARIAL", 11, "bold"), bg="navyblue",
                    fg="white", relief="raised", bd=5)
        br.pack()
        bt = Button(self.master, text="CLOSE", command=self.endprg6, font=("ARIAL", 11, "bold"), bg="#555555",
                    fg="white", relief="raised", bd=5)
        bt.pack()

        la1.place(x=190, y=100)
        e1.place(x=320, y=100)

        lb1.place(x=190, y=160)
        e2.place(x=320, y=160)

        b1.place(x=210, y=210)
        br.place(x=285, y=210)
        bt.place(x=365, y=210)

        self.second = Toplevel()
        self.second.geometry("900x450")
        self.second.configure(background="#9FC6CB")
        self.second.withdraw()

        self.usn = StringVar()
        self.username = StringVar()
        self.usernam1 = StringVar()
        self.usn = StringVar()
        self.grp = StringVar()
        self.sem = StringVar()
        self.dept = StringVar()
        self.eff = StringVar()
        self.impy = StringVar()
        self.cie1 = StringVar()
        self.cie2 = StringVar()
        self.sie = StringVar()
        self.sub1 = StringVar()
        self.sub2 = StringVar()
        self.sub3 = StringVar()
        self.sub4 = StringVar()
        self.sub5 = StringVar()
        self.sub6 = StringVar()
        self.sub7 = StringVar()
        self.sub8 = StringVar()
        self.sub9 = StringVar()
        self.sub11 = StringVar()
        self.sub22 = StringVar()
        self.att = StringVar()
        self.bak = StringVar()
        self.usn1 = StringVar()
        self.sub33 = StringVar()
        self.sub44 = StringVar()
        self.sub55 = StringVar()
        self.sub66 = StringVar()
        self.sub77 = StringVar()
        self.sub88 = StringVar()
        self.sub99 = StringVar()

        canvas = Canvas(self.second, width=150, height=150, border=0.5, bg="darkgrey", relief="groove", bd=5)
        canvas.configure(border=0.5)
        canvas.place(x=20, y=50)
        self.second.my_image = PhotoImage(file='C:\\Users\\hp\\Desktop\\PI.png')
        canvas.create_image(0, 0, anchor="nw", image=self.master.my_image)
        self.ptilte = Label(self.second, text="              STUDENT DETAILS DATABASE           ", bg="#DBE7FF",
                            font=('Imprint MT Shadow', 13, "bold"),
                            fg="navyblue", relief="groove").pack()
        Label(self.second, text="Department Of Computer Science & Engineering", font=("Imprint MT Shadow ", 16, "bold"),
              fg="maroon", bg="#F5FFCF").pack()

        l2 = Label(self.second, text="NAME:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e2 = Entry(self.second, textvariable=self.usernam1, fg="red", font=("", 11, "bold"), relief="sunken", bd=5,
                   bg="#F4FCE3", justify="center")
        l2.place(x=205, y=90)
        e2.place(x=290, y=93)
        l3 = Label(self.second, text="USN:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e3 = Entry(self.second, textvariable=self.usn1, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l3.place(x=590, y=90)
        e3.place(x=650, y=91)
        l4 = Label(self.second, text="DEPARTMENT:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e4 = Entry(self.second, textvariable=self.dept, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l4.place(x=500, y=130)
        e4.place(x=650, y=131)
        l5 = Label(self.second, text="SEMISTER:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e5 = Entry(self.second, textvariable=self.sem, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")

        l5.place(x=180, y=130)
        e5.place(x=290, y=131)

        l6 = Label(self.second, text="EFFICIENCY(%):", fg="navyblue", font=("Bookman Old Style", 13, "bold"),
                   bg="#9FC6CB")
        e6 = Entry(self.second, textvariable=self.eff, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l6.place(x=490, y=170)
        e6.place(x=650, y=171)
        l7 = Label(self.second, text="GPA:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e7 = Entry(self.second, textvariable=self.grp, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l7.place(x=215, y=170)
        e7.place(x=290, y=171)
        l8 = Label(self.second, text="IMPRVMT AREA:", fg="navyblue", font=("Bookman Old Style", 13, "bold"),
                   bg="#9FC6CB")
        e8 = Entry(self.second, textvariable=self.impy, fg="red", bg="white", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l8.place(x=490, y=218)
        e8.place(x=650, y=215)
        l9 = Label(self.second, text="ATTANDANCE:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e9 = Entry(self.second, textvariable=self.att, fg="red", bg="white", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l9.place(x=140, y=218)
        e9.place(x=290, y=215)
        l99 = Label(self.second, text="BACKLOG:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e99 = Entry(self.second, textvariable=self.bak, fg="red", bg="white", font=("", 11, "bold"), relief="sunken",
                    bd=5, justify="center")
        l99.place(x=350, y=260)
        e99.place(x=460, y=257)

        self.second.withdraw()
        self.second.protocol("WM_DELETE_WINDOW", self.endprg11)
        bt = Button(self.second, text="Next",command=self.next, font=("Bookman Old Style", 11, "bold"), bg="darkblue",
                    fg="white",
                    relief="raised", bd=5)
        bt.place(x=440, y=330)

        bt1 = Button(self.second, text="CLOSE", command=self.endprg1, font=("Bookman Old Style", 11, "bold"),
                     bg="darkblue",
                     relief="raised", bd=5,
                     fg="white")
        bt1.place(x=510, y=330)







        self.third=Toplevel()
        self.third.geometry("900x650")
        self.third.configure(background="#9FC6CB")
        self.third.withdraw()
        ca1 = Canvas(self.third, width=150, height=150, relief="ridge", bg="purple", bd=10)
        ca1.place(x=45, y=65)
        ca1.configure(border=0.5)
        self.my_image1 = PhotoImage(file='C:\\Users\\hp\\Desktop\\PI.png')
        ca1.create_image(0, 0, anchor="nw", image=self.my_image1)
        self.third.my_image = PhotoImage(file='C:\\Users\\hp\\Desktop\\PI.png')
        canvas.create_image(0, 0, anchor="nw", image=self.third.my_image)
        self.ptilte = Label(self.third, text="              STUDENT DETAILS DATABASE           ", bg="#DBE7FF",
                            font=('Imprint MT Shadow', 13, "bold"),
                            fg="navyblue", relief="groove").pack()
        Label(self.third, text="Department Of Computer Science & Engineering", font=("Imprint MT Shadow ", 16, "bold"),
              fg="maroon", bg="#F5FFCF").pack()
        Label(self.third, text="CIE AVG", font=("Bookman Old Style", 15, "bold"), fg="darkgreen").place(x=395, y=95)
        Label(self.third, text="SIE", font=("Bookman Old Style", 15, "bold"), fg="darkgreen").place(x=670, y=95)
        la1 = Label(self.third, text="SUB1:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la1.place(x=280, y=145)
        e1 = Entry(self.third, textvariable=self.sub1, bg="#F4FCE3", font=("Bookman Old Style", 11, "bold"),
                   relief="sunken", bd=4,
                   fg="red", justify="center")
        e1.place(x=350, y=145)
        la2 = Label(self.third, text="SUB2:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la2.place(x=280, y=180)
        e2 = Entry(self.third, textvariable=self.sub2, bg="#F4FCE3", font=("Bookman Old Style", 11, "bold"),
                   relief="sunken", bd=4,
                   fg="red", justify="center")
        e2.place(x=350, y=180)
        la3 = Label(self.third, text="SUB3:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la3.place(x=280, y=215)
        e3 = Entry(self.third, textvariable=self.sub3, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                   bg="#F4FCE3",
                   fg="red", justify="center")
        e3.place(x=350, y=215)
        la4 = Label(self.third, text="SUB4:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la4.place(x=280, y=250)
        e4 = Entry(self.third, textvariable=self.sub4, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                   bg="#F4FCE3",
                   fg="red", justify="center")
        e4.place(x=350, y=250)
        la5 = Label(self.third, text="SUB5:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la5.place(x=280, y=285)
        e5 = Entry(self.third, textvariable=self.sub5, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                   bg="#F4FCE3",
                   fg="red", justify="center")
        e5.place(x=350, y=285)
        la6 = Label(self.third, text="SUB6:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la6.place(x=280, y=325)
        e6 = Entry(self.third, textvariable=self.sub6, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                   bg="#F4FCE3",
                   fg="red", justify="center")
        e6.place(x=350, y=325)
        la7 = Label(self.third, text="LAB1:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la7.place(x=280, y=365)
        e33 = Entry(self.third, textvariable=self.sub7, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                    bg="#F4FCE3",
                    fg="red", justify="center")
        e33.place(x=350, y=365)
        la8 = Label(self.third, text="LAB2:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la8.place(x=280, y=400)
        e99 = Entry(self.third, textvariable=self.sub8, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                    bg="#F4FCE3",
                    fg="red", justify="center")
        e99.place(x=350, y=400)
        la9 = Label(self.third, text="PLACEMENT:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la9.place(x=215, y=440)
        e66 = Entry(self.third, textvariable=self.sub9, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                    bg="#F4FCE3",
                    fg="red", justify="center")
        e66.place(x=350, y=440)

        e7 = Entry(self.third, textvariable=self.sub11, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                   bg="#F4FCE3",
                   fg="red", justify="center")
        e7.place(x=580, y=145)
        e8 = Entry(self.third, textvariable=self.sub22, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                   bg="#F4FCE3",
                   fg="red", justify="center")
        e8.place(x=580, y=180)
        e = Entry(self.third, textvariable=self.sub33, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                  bg="#F4FCE3",
                  fg="red", justify="center")
        e.place(x=580, y=215)
        e9 = Entry(self.third, textvariable=self.sub44, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                   bg="#F4FCE3",
                   fg="red", justify="center")
        e9.place(x=580, y=250)
        e10 = Entry(self.third, textvariable=self.sub55, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                    bg="#F4FCE3",
                    fg="red", justify="center")
        e10.place(x=580, y=285)
        e11 = Entry(self.third, textvariable=self.sub66, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                    bg="#F4FCE3",
                    fg="red", justify="center")
        e11.place(x=580, y=325)
        e12 = Entry(self.third, textvariable=self.sub77, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                    bg="#F4FCE3",
                    fg="red", justify="center")
        e12.place(x=580, y=365)
        e13 = Entry(self.third, textvariable=self.sub88, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                    bg="#F4FCE3",
                    fg="red", justify="center")
        e13.place(x=580, y=400)
        e22 = Entry(self.third, textvariable=self.sub99, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                    bg="#F4FCE3",
                    fg="red", justify="center")
        e22.place(x=580, y=440)
        bt = Button(self.third, text="ADD", command=self.add, font=("Bookman Old Style", 11, "bold"), bg="darkblue",
                    fg="white",
                    relief="raised", bd=5)
        bt.place(x=440, y=480)

        bt1 = Button(self.third, text="CLOSE", command=self.endprg13, font=("Bookman Old Style", 11, "bold"),
                     bg="darkblue",
                     relief="raised", bd=5,
                     fg="white")
        bt1.place(x=510, y=480)
        bt1 = Button(self.third, text="BACK", command=self.back, font=("Bookman Old Style", 11, "bold"),
                     bg="darkblue",
                     relief="raised", bd=5,
                     fg="white")
        bt1.place(x=600, y=480)











    def login1(self):
        self.db = sqlite3.connect("ADMIN.db")
        self.c = self.db.cursor()
        self.sql = "SELECT * FROM login WHERE USER=? AND PASS=?"
        self.c.execute(self.sql, [(self.uname.get()), (self.passw3.get())])
        self.row = self.c.fetchone()
        if self.row:
            messagebox.showinfo("WELOCME", "Login Successfull")
            self.master.withdraw()
            self.second.deiconify()

        else:
            messagebox.showerror("ERROR", "Record Not Found\n Or\n Please Input Correct Username And Password")
            self.clear()

    def next(self):
        self.second.withdraw()
        self.third.deiconify()
    def back(self):
        self.third.withdraw()
        self.second.deiconify()

    def endprg13(self):
        self.third.destroy()
        self.second.destroy()
        self.master.destroy()

    def endprg6(self):
        self.master.destroy()

    def add(self):
        self.gh=sqlite3.connect("ADMIN.db")
        self.cc=self.gh.cursor()
        self.cc.execute("INSERT INTO INF(NAME,USN,SEMISTER,DEPARTMENT,GPA,EFFICIENCY,IMP_AREA,SUB1,SUB2,SUB3,SUB4,SUB5,SUB6,SUB7,SUB8,SUB9,ATTENDANCE,BACKLOG) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                  (self.usernam1.get(), self.usn1.get(),self.sem.get(),self.dept.get(),self.grp.get(),self.eff.get(),self.impy.get(),self.att.get(),self.bak.get(),
                   self.sub1.get(), self.sub2.get(), self.sub3.get(), self.sub4.get(), self.sub5.get(), self.sub6.get(),
                   self.sub7.get(), self.sub8.get(), self.sub9.get()))
        self.cc.execute("INSERT INTO c1(NAME,USN,SUB1,SUB2,SUB3,SUB4,SUB5,SUB6,LAB1,LAB2,PLMNT) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
            (self.usernam1.get(), self.usn1.get(),
             self.sub11.get(), self.sub22.get(), self.sub33.get(), self.sub44.get(), self.sub55.get(), self.sub66.get(),
             self.sub77.get(), self.sub88.get(), self.sub99.get()))
        self.cc.execute("INSERT INTO stuff(NAME,USN) VALUES(?,?)",(self.usernam1.get(),self.usn1.get()))
        self.gh.commit()




        self.gh.commit()
        messagebox.showinfo("STUDENT ENTRY","SUCCESSFULLY ADDED")
        self.clear1()

    def clear(self):
        self.uname.set('')
        self.passw3.set('')
    def clear1(self):
        self.usernam1.set('')
        self.usn1.set('')
        self.dept.set('')
        self.grp.set('')
        self.sem.set('')
        self.impy.set('')
        self.att.set('')
        self.bak.set('')
        self.eff.set('')
        self.sub1.set('')
        self.sub2.set('')
        self.sub3.set('')
        self.sub4.set('')
        self.sub5.set('')
        self.sub6.set('')
        self.sub7.set('')
        self.sub8.set('')
        self.sub9.set('')
        self.sub11.set('')
        self.sub22.set('')
        self.sub33.set('')
        self.sub44.set('')
        self.sub55.set('')
        self.sub66.set('')
        self.sub77.set('')
        self.sub88.set('')
        self.sub99.set('')



    def endprg11(self):
        self.second.destroy()
        self.master.destroy()
    def endprg1(self):

        self.second.destroy()
        self.master.destroy()

mw = Tk()
mw.geometry("600x350")
mw.configure(background="darkgrey",border=0.5)
mw.title("COMPUTER SCIENCE DEPARTMENT")
myapp = window(mw)
mw.mainloop()
