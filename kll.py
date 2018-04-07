from tkinter import *
from tkinter import messagebox
import sqlite3

class window:
    def __init__(self, master):
        self.master = master
        canvas = Canvas(self.master, width=100, height=100, border=0.5, bg="green")
        canvas.configure(border=0.5)
        canvas.place(x=50, y=70)
        self.master.my_image = PhotoImage(file='C:\\Users\\hp\\Downloads\\kl.png')
        canvas.create_image(0, 0, anchor="nw", image=self.master.my_image)
        self.passw = StringVar()
        self.usernam = StringVar()
        self.usernam1=StringVar()
        self.usn=StringVar()
        self.grp=StringVar()
        self.sem=StringVar()
        self.dept=StringVar()
        self.eff=StringVar()
        self.impy=StringVar()
        self.cie1=StringVar()
        self.cie2=StringVar()
        self.sie=StringVar()
        self.sub1=StringVar()
        self.sub2 = StringVar()
        self.sub3 = StringVar()
        self.sub4 = StringVar()
        self.sub5 = StringVar()
        self.sub6 = StringVar()
        self.sub7 = StringVar()
        self.sub8 = StringVar()
        self.sub9 = StringVar()

        self.ptilte = Label(self.master, text="               STUDENT LOGIN           ", bg="#DBE7FF", font=('ARIAL', 13, "bold"),
                       fg="navyblue")
        Label(self.master,text="Welcome To Computer Science Department", font=('ARIAL', 13, "bold"),fg="#C73866",bg="#F5FFCF").place(x=135,y=35)
        self.ptilte.pack()
        la1=Label(self.master, text="USERNAME:", fg="BLUE", font=("", 11, "bold"), bg="#F5FFCF")

        e1 = Entry(self.master, textvariable=self.usernam,fg="purple",font=("",10,"bold"))


        lb1=Label(self.master, text="PASSWORD: ", fg="RED", font=("", 11, "bold"), bg="#F5FFCF")


        e2 = Entry(self.master, textvariable=self.passw, show="*",fg="purple",font=("",10,"bold"))


        b1 = Button(self.master, text="Login", command=self.login,font=("ARIAL",11,"bold"), bg="#47D190",fg="white")
        b1.pack()
        br = Button(self.master, text="Clear", command=self.clear,font=("ARIAL",11,"bold"), bg="#47D190",fg="white")
        br.pack()
        bt = Button(self.master, text="Close", command=self.endprg,font=("ARIAL",11,"bold"), bg="#47D190",fg="white")
        bt.pack()

        la1.place(x=170, y=90)
        e1.place(x=270, y=90)

        lb1.place(x=170, y=130)
        e2.place(x=270, y=130)

        b1.place(x=200, y=175)
        br.place(x=260, y=175)
        bt.place(x=320, y=175)





























        self.second = Toplevel()
        self.second.geometry("800x400")
        self.second.configure(background="#F5FFCF")
        Label(self.second, text="STUDENT INFORMATION", bg="#DBE7FF", font=('ARIAL', 13, "bold"),fg="navyblue").place(x=320,y=35)
        Label(self.second, text="Welcome To Computer Science Department", font=('ARIAL', 13, "bold"), fg="#C73866",
              bg="#F5FFCF").pack()
        canvas = Canvas(self.second, width=100, height=100, border=0.5, bg="green")
        canvas.configure(border=0.5)
        canvas.place(x=25, y=40)
        self.my_image = PhotoImage(file='C:\\Users\\hp\\Downloads\\kl.png')
        canvas.create_image(0, 0, anchor="nw", image=self.my_image)


        l2=Label(self.second,text="NAME:",fg="NAVYBLUE", font=(None, 12, "bold"), bg="#F5FFCF")
        e2=Entry(self.second,textvariable=self.usernam1,fg="RED", bg="white",font=("",10,"bold"))
        l2.place(x=190, y=80)
        e2.place(x=270, y=83)
        l3 = Label(self.second, text="USN:",fg="NAVYBLUE", font=(None, 12, "bold"), bg="#F5FFCF")
        e3 = Entry(self.second, textvariable=self.usn,fg="RED", bg="white",font=("",10,"bold"))
        l3.place(x=440, y=80)
        e3.place(x=570, y=83)
        l4=Label(self.second,text="SEMISTER:",fg="GREEN", font=(None, 12, "bold"), bg="#F5FFCF")
        e4=Entry(self.second,textvariable=self.sem,fg="RED", bg="white",font=("",10,"bold"))
        l4.place(x=440, y=110)
        e4.place(x=570, y=113)
        l5 = Label(self.second, text="DEPARTMENT:",fg="GREEN", font=(None, 12, "bold"), bg="#F5FFCF")
        e5 = Entry(self.second, textvariable=self.dept,fg="RED", bg="white",font=("",10,"bold"))
        l5.place(x=140, y=110)
        e5.place(x=270, y=113)

        l5 = Label(self.second, text="CIE I:", fg="GREEN", font=(None, 12, "bold"), bg="white")
        e5 = Entry(self.second, textvariable=self.cie1, fg="RED", bg="white", font=("", 10, "bold"))
        l5.place(x=190, y=140)
        e5.place(x=270, y=143)
        l5 = Label(self.second, text="CIE II:", fg="GREEN", font=(None, 12, "bold"), bg="white")
        e5 = Entry(self.second, textvariable=self.cie2, fg="RED", bg="white", font=("", 10, "bold"))
        l5.place(x=440, y=140)
        e5.place(x=570, y=143)
        l5 = Label(self.second, text="SIE :", fg="GREEN", font=(None, 12, "bold"), bg="#F5FFCF")
        e5 = Entry(self.second, textvariable=self.sie, fg="RED", bg="white", font=("", 10, "bold"))
        l5.place(x=190, y=170)
        e5.place(x=270, y=173)
        l6 = Label(self.second, text="GPA:",fg="GREEN", font=(None, 12,"bold"), bg="#F5FFCF")
        e6 = Entry(self.second, textvariable=self.grp,fg="RED", bg="white",font=("",10,"bold"))
        l6.place(x=440, y=170)
        e6.place(x=570, y=173)
        l7 = Label(self.second, text="EFFENCY(%):",fg="GREEN", font=(None, 12, "bold"), bg="#F5FFCF")
        e7 = Entry(self.second, textvariable=self.eff,fg="RED", bg="white",font=("",10,"bold"))
        l7.place(x=150, y=200)
        e7.place(x=270, y=203)
        l8 = Label(self.second, text="IMPRVMT AREA:",fg="GREEN", font=(None, 12, "bold"), bg="#F5FFCF")
        e8 = Entry(self.second, textvariable=self.impy,fg="RED", bg="white",font=("",10,"bold"))
        l8.place(x=430, y=200)
        e8.place(x=570, y=203)

        self.second.withdraw()
        self.second.protocol("WM_DELETE_WINDOW", self.endprg)
        bt = Button(self.second, text="Close", command=self.endprg,font=("ARIAL",11,"bold"), bg="#47D190",fg="white")
        bt.place(x=390,y=240)

    def clear(self):
        self.usernam.set('')
        self.passw.set('')

    def endprg(self):
        self.master.destroy()



    def login(self):
        self.db = sqlite3.connect("STDLOGIN.db")
        self.c = self.db.cursor()
        self.sql = "SELECT * FROM stuff WHERE PASSWORD=?"
        self.c.execute(self.sql, [(self.passw.get())])
        self.row = self.c.fetchone()
        if self.row:
            self.cer = "SELECT * FROM INF WHERE NAME=? AND PASSWORD=?"
            self.c.execute(self.cer, [(self.usernam.get()), (self.passw.get())])
            self.row1 = self.c.fetchone()
            if self.row1:
                messagebox.showinfo("WELCOME", "Record Found")
                self.usernam1.set(self.row1[0])
                self.usn.set(self.row1[1])
                self.sem.set(self.row1[2])
                self.dept.set(self.row1[3])
                self.cie1.set(self.row1[4])
                self.cie2.set(self.row1[5])
                self.sie.set(self.row1[6])
                self.grp.set(self.row1[7])
                self.eff.set(self.row1[8])
                self.impy.set(self.row1[9])
                self.master.withdraw()
                self.second.deiconify()
                self.clear()
            else:
                messagebox.showerror("ERROR", "Record Not Found\n Or\n Please Input Correct Username And Password")
                self.clear()


        else:
            messagebox.showerror("ERROR", "Record Not Found\n Or\n Please Input Correct Username And Password")
            self.endprg1()


    def endprg1(self):
        self.second.destroy()
        self.master.destroy()



mw = Tk()
mw.geometry("600x400")
mw.configure(background="#F5FFCF",border=0.5)
mw.title("COMPUTER SCIENCE DEPARTMENT")
myapp = window(mw)
mw.mainloop()
