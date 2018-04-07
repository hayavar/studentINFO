from tkinter import *
from tkinter import messagebox
import sqlite3

class window:
    def __init__(self, master):
        self.master = master
        canvas = Canvas(self.master, width=150, height=150, border=0.5, bg="navyblue",relief="groove",bd=5)
        canvas.configure(border=0.5)
        canvas.place(x=20, y=75)
        self.master.my_image = PhotoImage(file='C:\\Users\\hp\\Documents\\pic1.png')
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
        self.sub11 = StringVar()
        self.sub22= StringVar()
        self.sub33 = StringVar()
        self.sub44 = StringVar()
        self.sub55 = StringVar()
        self.sub66 = StringVar()
        self.sub77 = StringVar()
        self.sub88 = StringVar()
        self.sub99 = StringVar()
        self.att=StringVar()
        self.bak=StringVar()

        self.ptilte = Label(self.master, text="               STUDENT LOGIN           ", bg="#DBE7FF", font=('Imprint MT Shadow', 13, "bold"),
                       fg="navyblue",relief="groove")
        Label(self.master,text="Department Of Computer Science & Engineering", font=('Imprint MT Shadow ', 16, "bold"),fg="maroon",bg="darkgrey").place(x=70,y=30)
        self.ptilte.pack()
        la1=Label(self.master, text="USERNAME:", fg="white", font=("", 14, "bold"), bg="darkgrey")

        e1 = Entry(self.master, textvariable=self.usernam,fg="navyblue",font=("",11,"bold"),relief="sunken",bd=5,bg="#F4FCE3")


        lb1=Label(self.master, text="PASSWORD: ", fg="RED", font=("", 14, "bold"), bg="darkgrey")


        e2 = Entry(self.master, textvariable=self.passw, show="*",fg="navyblue",font=("",11,"bold"),relief="sunken",bd=5,bg="#F4FCE3")


        b1 = Button(self.master, text="LOGIN", command=self.login,font=("ARIAL",11,"bold"), bg="#555555",fg="white",relief="raised",bd=5)
        b1.pack()
        br = Button(self.master, text="CLEAR", command=self.clear,font=("ARIAL",11,"bold"), bg="navyblue",fg="white",relief="raised",bd=5)
        br.pack()
        bt = Button(self.master, text="CLOSE", command=self.endprg,font=("ARIAL",11,"bold"), bg="#555555",fg="white",relief="raised",bd=5)
        bt.pack()

        la1.place(x=190, y=100)
        e1.place(x=320, y=100)

        lb1.place(x=190, y=160)
        e2.place(x=320, y=160)

        b1.place(x=210, y=210)
        br.place(x=285, y=210)
        bt.place(x=365, y=210)





























        self.second = Toplevel()
        self.second.geometry("900x400")
        self.second.configure(background="#9FC6CB")
        Label(self.second, text="Department Of Computer Science & Engineering", font=('Times New Roman', 13, "bold"),
              fg="#C73866",
              bg="#F5FFCF", relief="groove", bd=5).pack()
        Label(self.second, text="STUDENT INFORMATION", bg="#DBE7FF", font=('Imprint MT Shadow', 12, "bold"),fg="navyblue",relief="groove",bd=5).pack()


        canvas = Canvas(self.second, width=100, height=100,relief="ridge",bg="purple", bd=10)
        canvas.configure(border=0.5)
        canvas.place(x=25, y=40)
        self.my_image = PhotoImage(file='C:\\Users\\hp\\Downloads\\kl.png')
        canvas.create_image(0, 0, anchor="nw", image=self.my_image)



        l2=Label(self.second,text="NAME:",fg="navyblue", font=(None, 13, "bold"), bg="#9FC6CB")
        e2=Entry(self.second,textvariable=self.usernam1,fg="red",font=("",11,"bold"),relief="sunken",bd=5,bg="#F4FCE3",justify="center")
        l2.place(x=205, y=80)
        e2.place(x=270, y=83)
        l3 = Label(self.second, text="USN:",fg="navyblue", font=(None, 13, "bold"), bg="#9FC6CB")
        e3 = Entry(self.second, textvariable=self.usn,fg="red",bg="#F4FCE3",font=("",11,"bold"),relief="sunken",bd=5,justify="center")
        l3.place(x=580, y=80)
        e3.place(x=630, y=81)
        l4=Label(self.second,text="SEMISTER:",fg="navyblue", font=(None, 13, "bold"), bg="#9FC6CB")
        e4=Entry(self.second,textvariable=self.sem,fg="red",bg="#F4FCE3",font=("",11,"bold"),relief="sunken",bd=5,justify="center")
        l4.place(x=530, y=120)
        e4.place(x=630, y=121)
        l5 = Label(self.second, text="DEPARTMENT:",fg="navyblue", font=(None, 13, "bold"), bg="#9FC6CB")
        e5 = Entry(self.second, textvariable=self.dept,fg="red",bg="#F4FCE3",font=("",11,"bold"),relief="sunken",bd=5,justify="center")
        l5.place(x=140, y=120)
        e5.place(x=270, y=121)

        l6 = Label(self.second, text="EFFICIENCY(%):",fg="navyblue", font=(None, 13,"bold"), bg="#9FC6CB")
        e6 = Entry(self.second, textvariable=self.eff,fg="red",bg="#F4FCE3",font=("",11,"bold"),relief="sunken",bd=5,justify="center")
        l6.place(x=490, y=160)
        e6.place(x=630, y=161)
        l7 = Label(self.second, text="GPA:",fg="navyblue", font=(None, 13, "bold"), bg="#9FC6CB")
        e7 = Entry(self.second, textvariable=self.grp,fg="red",bg="#F4FCE3",font=("",11,"bold"),relief="sunken",bd=5,justify="center")
        l7.place(x=215, y=160)
        e7.place(x=270, y=161)
        l8 = Label(self.second, text="IMPRVMT AREA:",fg="navyblue", font=(None, 13, "bold"), bg="#9FC6CB")
        e8 = Entry(self.second, textvariable=self.impy,fg="red" ,bg="white",font=("",11,"bold"),relief="sunken",bd=5,justify="center")
        l8.place(x=490, y=208)
        e8.place(x=630, y=205)
        l9 = Label(self.second, text="ATTANDANCE:", fg="navyblue", font=(None, 13, "bold"), bg="#9FC6CB")
        e9 = Entry(self.second, textvariable=self.att, fg="red", bg="white", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l9.place(x=140, y=208)
        e9.place(x=270, y=205)
        l99 = Label(self.second, text="BACKLOG:", fg="navyblue", font=(None, 13, "bold"), bg="#9FC6CB")
        e99 = Entry(self.second, textvariable=self.bak, fg="red", bg="white", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l99.place(x=350, y=250)
        e99.place(x=450, y=247)

        self.second.withdraw()
        self.second.protocol("WM_DELETE_WINDOW", self.endprg)
        Label(self.second,text="View Marks Card?",fg="purple", font=(None, 13, "bold","italic"), bg="white").place(x=280,y=328)
        bt = Button(self.second, text="VIEW", command=self.next,font=("ARIAL",11,"bold"), bg="darkblue",fg="white",relief="raised",bd=5)
        bt.place(x=440,y=320)
        bt1 = Button(self.second, text="CLOSE", command=self.endprg1, font=("ARIAL", 11, "bold"), bg="darkblue",relief="raised",bd=5,
                     fg="white")
        bt1.place(x=510, y=320)




        self.third=Toplevel()
        self.third.configure(bg="#CCD8F0")
        Label(self.third, text="Department Of Computer Science & Engineering",
              font=('Times New Roman', 14, "bold"), fg="#C73866",
              bg="#F5FFCF", relief="groove", bd=5).pack()
        Label(self.third, text="   MARKS SHEET   ",
              font=('Imprint MT Shadow', 14, "bold"), fg="navyblue",
              bg="lightblue", relief="groove", bd=5).pack()

        ca1=Canvas(self.third,width=150,height=150,relief="ridge",bg="purple",bd=10)
        ca1.place(x=45,y=65)
        ca1.configure(border=0.5)
        self.my_image1 = PhotoImage(file='C:\\Users\\hp\\Documents\\pic1.png')
        ca1.create_image(0,0,anchor="nw",image=self.my_image1)
        bt = Button(self.third, text="CLOSE", command=self.endprg2, font=("ARIAL", 11, "bold"), bg="#555555", fg="white",
                    relief="raised", bd=5)
        bt.place(x=460, y=490)

        bt2=Button(self.third,text="BACK",command=self.back, font=("ARIAL", 11, "bold"), bg="darkblue", fg="white",
                    relief="raised", bd=5)
        bt2.place(x=540,y=490)
        self.third.geometry("900x600")
        self.third.withdraw()
        self.third.protocol("WM_DELETE_WINDOW", self.endprg)

    def clear(self):
        self.usernam.set('')
        self.passw.set('')

    def endprg(self):
        self.master.destroy()

    def back(self):
        self.third.withdraw()
        self.second.deiconify()
        self.master.withdraw()

    def next(self):
        self.master.withdraw()
        self.second.withdraw()
        self.third.deiconify()

        Label(self.third,text="CIE AVG",font=("arial",15,"bold"),fg="darkgreen").place(x=395,y=95)
        Label(self.third,text="SIE",font=("arial",15,"bold"),fg="darkgreen").place(x=620,y=95)
        la1 = Label(self.third, text="SUB1:",bg="#DBE7FF",font=("arial",12,"bold"),fg="navyblue")
        la1.place(x=280,y=145)
        e1 = Entry(self.third, textvariable=self.sub1,bg="#F4FCE3",font=("",11,"bold"),relief="sunken",bd=4,fg="red",justify="center")
        e1.place(x=350,y=145)
        la2 = Label(self.third, text="SUB2:",bg="#DBE7FF",font=("arial",12,"bold"),fg="navyblue")
        la2.place(x=280,y=180)
        e2 = Entry(self.third, textvariable=self.sub2,bg="#F4FCE3",font=("",11,"bold"),relief="sunken",bd=4,fg="red",justify="center")
        e2.place(x=350,y=180)
        la3 = Label(self.third, text="SUB3:",bg="#DBE7FF",font=("arial",12,"bold"),fg="navyblue")
        la3.place(x=280,y=215)
        e3 = Entry(self.third, textvariable=self.sub3,font=("",11,"bold"),relief="sunken",bd=4,bg="#F4FCE3",fg="red",justify="center")
        e3.place(x=350,y=215)
        la4 = Label(self.third, text="SUB4:",bg="#DBE7FF",font=("arial",12,"bold"),fg="navyblue")
        la4.place(x=280,y=250)
        e4 = Entry(self.third, textvariable=self.sub4,font=("",11,"bold"),relief="sunken",bd=4,bg="#F4FCE3",fg="red",justify="center")
        e4.place(x=350,y=250)
        la5 = Label(self.third, text="SUB5:",bg="#DBE7FF",font=("arial",12,"bold"),fg="navyblue")
        la5.place(x=280,y=285)
        e5= Entry(self.third, textvariable=self.sub5,font=("",11,"bold"),relief="sunken",bd=4,bg="#F4FCE3",fg="red",justify="center")
        e5.place(x=350,y=285)
        la6 = Label(self.third, text="SUB6:",bg="#DBE7FF",font=("arial",12,"bold"),fg="navyblue")
        la6.place(x=280,y=325)
        e6= Entry(self.third, textvariable=self.sub6,font=("",11,"bold"),relief="sunken",bd=4,bg="#F4FCE3",fg="red",justify="center")
        e6.place(x=350,y=325)
        la7 = Label(self.third, text="LAB1:",bg="#DBE7FF",font=("arial",12,"bold"),fg="navyblue")
        la7.place(x=280,y=365)
        e33 = Entry(self.third, textvariable=self.sub7,font=("",11,"bold"),relief="sunken",bd=4,bg="#F4FCE3",fg="red",justify="center")
        e33.place(x=350,y=365)
        la8 = Label(self.third, text="LAB2:",bg="#DBE7FF",font=("arial",12,"bold"),fg="navyblue")
        la8.place(x=280,y=400)
        e99 = Entry(self.third, textvariable=self.sub8,font=("",11,"bold"),relief="sunken",bd=4,bg="#F4FCE3",fg="red",justify="center")
        e99.place(x=350,y=400)
        la9 = Label(self.third, text="PLACEMENT:",bg="#DBE7FF",font=("arial",12,"bold"),fg="navyblue")
        la9.place(x=230,y=440)
        e66 = Entry(self.third, textvariable=self.sub9,font=("",11,"bold"),relief="sunken",bd=4,bg="#F4FCE3",fg="red",justify="center")
        e66.place(x=350,y=440)


        e7 = Entry(self.third, textvariable=self.sub11,font=("",11,"bold"),relief="sunken",bd=4,bg="#F4FCE3",fg="red",justify="center")
        e7.place(x=550,y=145)
        e8 = Entry(self.third, textvariable=self.sub22,font=("",11,"bold"),relief="sunken",bd=4,bg="#F4FCE3",fg="red",justify="center")
        e8.place(x=550, y=180)
        e = Entry(self.third, textvariable=self.sub33,font=("",11,"bold"),relief="sunken",bd=4,bg="#F4FCE3",fg="red",justify="center")
        e.place(x=550, y=215)
        e9 = Entry(self.third, textvariable=self.sub44,font=("",11,"bold"),relief="sunken",bd=4,bg="#F4FCE3",fg="red",justify="center")
        e9.place(x=550, y=250)
        e10 = Entry(self.third, textvariable=self.sub55,font=("",11,"bold"),relief="sunken",bd=4,bg="#F4FCE3",fg="red",justify="center")
        e10.place(x=550, y=285)
        e11 = Entry(self.third, textvariable=self.sub66,font=("",11,"bold"),relief="sunken",bd=4,bg="#F4FCE3",fg="red",justify="center")
        e11.place(x=550, y=325)
        e12 = Entry(self.third, textvariable=self.sub77,font=("",11,"bold"),relief="sunken",bd=4,bg="#F4FCE3",fg="red",justify="center")
        e12.place(x=550, y=365)
        e13 = Entry(self.third, textvariable=self.sub88,font=("",11,"bold"),relief="sunken",bd=4,bg="#F4FCE3",fg="red",justify="center")
        e13.place(x=550, y=400)
        e22 = Entry(self.third, textvariable=self.sub99,font=("",11,"bold"),relief="sunken",bd=4,bg="#F4FCE3",fg="red",justify="center")
        e22.place(x=550, y=440)




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
                self.sub1.set(self.row1[11])
                self.sub2.set(self.row1[12])
                self.sub3.set(self.row1[13])
                self.sub4.set(self.row1[14])
                self.sub5.set(self.row1[15])
                self.sub6.set(self.row1[16])
                self.sub7.set(self.row1[17])
                self.sub8.set(self.row1[18])
                self.sub9.set(self.row1[19])
                self.att.set((self.row1[20]))
                self.bak.set(self.row1[21])
                self.cer = "SELECT * FROM c1 WHERE NAME=? AND PASSWORD=?"
                self.c.execute(self.cer, [(self.usernam.get()), (self.passw.get())])
                self.row11 = self.c.fetchone()
                if self.row11:
                    self.sub11.set(self.row11[1])
                    self.sub22.set(self.row11[2])
                    self.sub33.set(self.row11[3])
                    self.sub44.set(self.row11[4])
                    self.sub55.set(self.row11[5])
                    self.sub66.set(self.row11[6])
                    self.sub77.set(self.row11[7])
                    self.sub88.set(self.row11[8])
                    self.sub99.set(self.row11[9])


                else:
                    messagebox.showerror()
                    self.clear()
                self.master.withdraw()
                self.second.deiconify()
                self.clear()
            else:
                messagebox.showerror("ERROR", "Record Not Found\n Or\n Please Input Correct Username And Password")
                self.clear()


        else:
            messagebox.showerror("ERROR", "Record Not Found\n Or\n Please Input Correct Username And Password")
            self.clear()


    def endprg1(self):
        self.second.destroy()
        self.master.destroy()
    def endprg2(self):
        self.third.destroy()
        self.second.destroy()
        self.master.destroy()



mw = Tk()
mw.geometry("600x400")
mw.configure(background="darkgrey",border=0.5)
mw.title("COMPUTER SCIENCE DEPARTMENT")
myapp = window(mw)
mw.mainloop()
