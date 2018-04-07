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
        self.uname=StringVar()
        self.passw3=StringVar()
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
        b1 = Button(self.master, text="LOGIN", command=self.login1, font=("ARIAL", 11, "bold"), bg="#555555", fg="white",
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
        self.second.geometry("600x350")
        self.second.configure(background="darkgrey")
        self.second.withdraw()

        canvas = Canvas(self.second, width=150, height=150, border=0.5, bg="darkgrey",relief="groove",bd=5)
        canvas.configure(border=0.5)
        canvas.place(x=20, y=75)
        self.second.my_image = PhotoImage(file='C:\\Users\\hp\\Desktop\\PI.png')
        canvas.create_image(0, 0, anchor="nw", image=self.master.my_image)
        self.usn = StringVar()
        self.username=StringVar()
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
        self.usn1=StringVar()
        self.sub33 = StringVar()
        self.sub44 = StringVar()
        self.sub55 = StringVar()
        self.sub66 = StringVar()
        self.sub77 = StringVar()
        self.sub88 = StringVar()
        self.sub99 = StringVar()

        self.usernam11 = StringVar()
        self.usn12 = StringVar()
        self.grp1 = StringVar()
        self.sem1 = StringVar()
        self.dept1 = StringVar()
        self.eff1 = StringVar()
        self.impy1 = StringVar()
        self.sub111 = StringVar()
        self.sub222 = StringVar()
        self.sub333 = StringVar()
        self.sub444 = StringVar()
        self.sub555 = StringVar()
        self.sub666 = StringVar()
        self.sub777 = StringVar()
        self.sub888 = StringVar()
        self.sub999 = StringVar()
        self.sub1111 = StringVar()
        self.sub2222 = StringVar()
        self.attt = StringVar()
        self.bakk = StringVar()
        self.usn12 = StringVar()
        self.sub3333 = StringVar()
        self.sub4444 = StringVar()
        self.sub5555 = StringVar()
        self.sub6666 = StringVar()
        self.sub7777 = StringVar()
        self.sub8888 = StringVar()
        self.sub9999 = StringVar()



        self.ptilte = Label(self.second, text="               ADMIN LOGIN           ", bg="#DBE7FF",
                            font=('Imprint MT Shadow', 13, "bold"),
                            fg="navyblue", relief="groove")
        Label(self.second, text="Department Of Computer Science & Engineering", font=("Imprint MT Shadow ", 16, "bold"),
              fg="maroon", bg="darkgrey").place(x=70, y=30)
        self.ptilte.pack()


        lb1 = Label(self.second, text="NAME: ", fg="#000033", font=("Bookman Old Style", 14, "bold"), bg="darkgrey")

        e2 = Entry(self.second, textvariable=self.username, fg="black", font=("ARIAL", 11, "bold"),
                   relief="sunken", bd=5, bg="#F4FCE3")


        la1 = Label(self.second, text="USN:", fg="#000033", font=("Bookman Old Style", 14, "bold"), bg="darkgrey")
        e1 = Entry(self.second, textvariable=self.usn, fg="black", font=("", 11, "bold"), relief="sunken", bd=5,
                   bg="#F4FCE3")

        br = Button(self.second, text="CLEAR", command=self.clear, font=("ARIAL", 11, "bold"), bg="navyblue",
                    fg="white", relief="raised", bd=5)
        br.pack()

        b1 = Button(self.second, text="LOGIN", command=self.login, font=("Bookman Old Style", 11, "bold"), bg="#555555", fg="WHITE",
                    relief="raised", bd=5)
        b1.pack()
        bt12 = Button(self.second, text="CLOSE", command=self.endprg11, font=("Bookman Old Style", 11, "bold"),
                     bg="#555555",
                     relief="raised", bd=5,
                     fg="white")
        bt1 = Button(self.second, text="ADD STUDENT", command=self.add, font=("Bookman Old Style", 11, "bold"),
                     bg="#555555",
                     relief="raised", bd=5,
                     fg="white")
        la1.place(x=250, y=160)
        e1.place(x=320, y=160)

        lb1.place(x=240, y=100)
        e2.place(x=320, y=100)

        b1.place(x=210, y=210)
        br.place(x=290, y=210)
        bt12.place(x=365, y=210)
        bt1.place(x=270, y=260)



        self.third = Toplevel()
        self.third.geometry("900x400")
        self.third.configure(background="#9FC6CB")
        Label(self.third, text="Department Of Computer Science & Engineering", font=('Times New Roman', 13, "bold"),
              fg="#C73866",
              bg="#F5FFCF", relief="groove", bd=5).pack()
        Label(self.third, text="STUDENT INFORMATION", bg="#DBE7FF", font=('Imprint MT Shadow', 12, "bold"),
              fg="navyblue", relief="groove", bd=5).pack()

        canvas = Canvas(self.third, width=150, height=150, relief="ridge", bg="purple", bd=10)
        canvas.configure(border=0.5)
        canvas.place(x=20, y=40)
        self.my_image = PhotoImage(file='C:\\Users\\hp\\Desktop\\PI.png')
        canvas.create_image(0, 0, anchor="nw", image=self.my_image)

        l2 = Label(self.third, text="NAME:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e2 = Entry(self.third, textvariable=self.usernam1, fg="red", font=("", 11, "bold"), relief="sunken", bd=5,
                   bg="#F4FCE3", justify="center")
        l2.place(x=205, y=80)
        e2.place(x=290, y=83)
        l3 = Label(self.third, text="USN:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e3 = Entry(self.third, textvariable=self.usn1, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l3.place(x=590, y=80)
        e3.place(x=650, y=81)
        l4 = Label(self.third, text="DEPARTMENT:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e4 = Entry(self.third, textvariable=self.dept, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l4.place(x=500, y=120)
        e4.place(x=650, y=121)
        l5 = Label(self.third, text="SEMISTER:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e5 = Entry(self.third, textvariable=self.sem, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")


        l5.place(x=180, y=120)
        e5.place(x=290, y=121)

        l6 = Label(self.third, text="EFFICIENCY(%):", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e6 = Entry(self.third, textvariable=self.eff, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l6.place(x=490, y=160)
        e6.place(x=650, y=161)
        l7 = Label(self.third, text="GPA:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e7 = Entry(self.third, textvariable=self.grp, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l7.place(x=215, y=160)
        e7.place(x=290, y=161)
        l8 = Label(self.third, text="IMPRVMT AREA:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e8 = Entry(self.third, textvariable=self.impy, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l8.place(x=490, y=208)
        e8.place(x=650, y=205)
        l9 = Label(self.third, text="ATTANDANCE:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e9 = Entry(self.third, textvariable=self.att, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l9.place(x=140, y=208)
        e9.place(x=290, y=205)
        l99 = Label(self.third, text="BACKLOG:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e99 = Entry(self.third, textvariable=self.bak, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                    bd=5, justify="center")
        l99.place(x=350, y=250)
        e99.place(x=460, y=247)

        self.third.withdraw()
        self.second.protocol("WM_DELETE_WINDOW", self.endprg11)
        Label(self.third, text="View Marks Card?", fg="purple", font=("Bookman Old Style", 13, "bold", "italic"), bg="white").place(
            x=250, y=328)
        bt = Button(self.third, text="VIEW", command=self.next, font=("Bookman Old Style", 11, "bold"), bg="darkblue", fg="white",
                    relief="raised", bd=5)
        bt.place(x=440, y=320)

        bt1 = Button(self.third, text="CLOSE", command=self.endprg1, font=("Bookman Old Style", 11, "bold"), bg="darkblue",
                     relief="raised", bd=5,
                     fg="white")
        bt1.place(x=510, y=320)
        bt1 = Button(self.third, text="BACK", command=self.back1, font=("Bookman Old Style", 11, "bold"),
                     bg="darkblue",
                     relief="raised", bd=5,
                     fg="white")
        bt1.place(x=590, y=320)








        self.four = Toplevel()
        self.four.configure(bg="#CCD8F0")
        Label(self.four, text="Department Of Computer Science & Engineering",
              font=('Times New Roman', 14, "bold"), fg="#C73866",
              bg="#F5FFCF", relief="groove", bd=5).pack()
        Label(self.four, text="   MARKS SHEET   ",
              font=('Imprint MT Shadow', 14, "bold"), fg="navyblue",
              bg="lightblue", relief="groove", bd=5).pack()

        ca1 = Canvas(self.four, width=150, height=150, relief="ridge", bg="purple", bd=10)
        ca1.place(x=45, y=65)
        ca1.configure(border=0.5)
        self.my_image1 = PhotoImage(file='C:\\Users\\hp\\Desktop\\PI.png')
        ca1.create_image(0, 0, anchor="nw", image=self.my_image1)
        bt = Button(self.four, text="CLOSE", command=self.endprg2, font=("Bookman Old Style", 11, "bold"), bg="#555555",
                    fg="white",
                    relief="raised", bd=5)
        bt.place(x=460, y=490)

        bt2 = Button(self.four, text="BACK", command=self.back, font=("Bookman Old Style", 11, "bold"), bg="darkblue", fg="white",
                     relief="raised", bd=5)
        bt2.place(x=540, y=490)
        self.four.geometry("900x600")
        self.four.withdraw()
        self.four.protocol("WM_DELETE_WINDOW", self.endprg12)

        Label(self.four, text="CIE AVG", font=("Bookman Old Style", 15, "bold"), fg="darkgreen").place(x=395, y=95)
        Label(self.four, text="SIE", font=("Bookman Old Style", 15, "bold"), fg="darkgreen").place(x=670, y=95)
        la1 = Label(self.four, text="SUB1:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la1.place(x=280, y=145)
        e1 = Entry(self.four, textvariable=self.sub1, bg="#F4FCE3", font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                   fg="red", justify="center")
        e1.place(x=350, y=145)
        la2 = Label(self.four, text="SUB2:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la2.place(x=280, y=180)
        e2 = Entry(self.four, textvariable=self.sub2, bg="#F4FCE3", font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                   fg="red", justify="center")
        e2.place(x=350, y=180)
        la3 = Label(self.four, text="SUB3:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la3.place(x=280, y=215)
        e3 = Entry(self.four, textvariable=self.sub3, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4, bg="#F4FCE3",
                   fg="red", justify="center")
        e3.place(x=350, y=215)
        la4 = Label(self.four, text="SUB4:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la4.place(x=280, y=250)
        e4 = Entry(self.four, textvariable=self.sub4, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4, bg="#F4FCE3",
                   fg="red", justify="center")
        e4.place(x=350, y=250)
        la5 = Label(self.four, text="SUB5:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la5.place(x=280, y=285)
        e5 = Entry(self.four, textvariable=self.sub5, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4, bg="#F4FCE3",
                   fg="red", justify="center")
        e5.place(x=350, y=285)
        la6 = Label(self.four, text="SUB6:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la6.place(x=280, y=325)
        e6 = Entry(self.four, textvariable=self.sub6, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4, bg="#F4FCE3",
                   fg="red", justify="center")
        e6.place(x=350, y=325)
        la7 = Label(self.four, text="LAB1:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la7.place(x=280, y=365)
        e33 = Entry(self.four, textvariable=self.sub7, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4, bg="#F4FCE3",
                    fg="red", justify="center")
        e33.place(x=350, y=365)
        la8 = Label(self.four, text="LAB2:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la8.place(x=280, y=400)
        e99 = Entry(self.four, textvariable=self.sub8, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4, bg="#F4FCE3",
                    fg="red", justify="center")
        e99.place(x=350, y=400)
        la9 = Label(self.four, text="PLACEMENT:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la9.place(x=215, y=440)
        e66 = Entry(self.four, textvariable=self.sub9, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4, bg="#F4FCE3",
                    fg="red", justify="center")
        e66.place(x=350, y=440)

        e7 = Entry(self.four, textvariable=self.sub11, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4, bg="#F4FCE3",
                   fg="red", justify="center")
        e7.place(x=580, y=145)
        e8 = Entry(self.four, textvariable=self.sub22, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4, bg="#F4FCE3",
                   fg="red", justify="center")
        e8.place(x=580, y=180)
        e = Entry(self.four, textvariable=self.sub33, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4, bg="#F4FCE3",
                  fg="red", justify="center")
        e.place(x=580, y=215)
        e9 = Entry(self.four, textvariable=self.sub44, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4, bg="#F4FCE3",
                   fg="red", justify="center")
        e9.place(x=580, y=250)
        e10 = Entry(self.four, textvariable=self.sub55, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4, bg="#F4FCE3",
                    fg="red", justify="center")
        e10.place(x=580, y=285)
        e11 = Entry(self.four, textvariable=self.sub66, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4, bg="#F4FCE3",
                    fg="red", justify="center")
        e11.place(x=580, y=325)
        e12 = Entry(self.four, textvariable=self.sub77, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4, bg="#F4FCE3",
                    fg="red", justify="center")
        e12.place(x=580, y=365)
        e13 = Entry(self.four, textvariable=self.sub88, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4, bg="#F4FCE3",
                    fg="red", justify="center")
        e13.place(x=580, y=400)
        e22 = Entry(self.four, textvariable=self.sub99, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4, bg="#F4FCE3",
                    fg="red", justify="center")
        e22.place(x=580, y=440)



        self.five=Toplevel()
        self.five.geometry("900x450")
        self.five.withdraw()
        self.five.configure(background="#9FC6CB")
        self.five.protocol("WM_DELETE_WINDOW", self.endprg15)
        canvas345 = Canvas(self.five, width=150, height=150, border=0.5, bg="darkgrey", relief="groove", bd=5)
        canvas345.configure(border=0.5)
        canvas345.place(x=20, y=50)
        self.five.my_image = PhotoImage(file='C:\\Users\\hp\\Desktop\\PI.png')
        canvas345.create_image(0, 0, anchor="nw", image=self.five.my_image)
        self.ptilte = Label(self.five, text="              STUDENT DETAILS DATABASE           ", bg="#DBE7FF",
                            font=('Imprint MT Shadow', 13, "bold"),
                            fg="navyblue", relief="groove").pack()
        Label(self.five, text="Department Of Computer Science & Engineering", font=("Imprint MT Shadow ", 16, "bold"),
              fg="maroon", bg="#F5FFCF").pack()

        l2 = Label(self.five, text="NAME:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e2 = Entry(self.five, textvariable=self.usernam11, fg="red", font=("", 11, "bold"), relief="sunken", bd=5,
                   bg="#F4FCE3", justify="center")
        l2.place(x=205, y=90)
        e2.place(x=290, y=93)
        l3 = Label(self.five, text="USN:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e3 = Entry(self.five, textvariable=self.usn12, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l3.place(x=590, y=90)
        e3.place(x=650, y=91)
        l4 = Label(self.five, text="DEPARTMENT:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e4 = Entry(self.five, textvariable=self.dept1, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l4.place(x=500, y=130)
        e4.place(x=650, y=131)
        l5 = Label(self.five, text="SEMISTER:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e5 = Entry(self.five, textvariable=self.sem1, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")

        l5.place(x=180, y=130)
        e5.place(x=290, y=131)

        l6 = Label(self.five, text="EFFICIENCY(%):", fg="navyblue", font=("Bookman Old Style", 13, "bold"),
                   bg="#9FC6CB")
        e6 = Entry(self.five, textvariable=self.eff1, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l6.place(x=490, y=170)
        e6.place(x=650, y=171)
        l7 = Label(self.five, text="GPA:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e7 = Entry(self.five, textvariable=self.grp1, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l7.place(x=215, y=170)
        e7.place(x=290, y=171)
        l8 = Label(self.five, text="IMPRVMT AREA:", fg="navyblue", font=("Bookman Old Style", 13, "bold"),
                   bg="#9FC6CB")
        e8 = Entry(self.five, textvariable=self.impy1, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l8.place(x=490, y=218)
        e8.place(x=650, y=215)
        l9 = Label(self.five, text="ATTANDANCE:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e9 = Entry(self.five, textvariable=self.attt, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                   bd=5, justify="center")
        l9.place(x=140, y=218)
        e9.place(x=290, y=215)
        l99 = Label(self.five, text="BACKLOG:", fg="navyblue", font=("Bookman Old Style", 13, "bold"), bg="#9FC6CB")
        e99 = Entry(self.five, textvariable=self.bakk, fg="red", bg="#F4FCE3", font=("", 11, "bold"), relief="sunken",
                    bd=5, justify="center")
        l99.place(x=350, y=260)
        e99.place(x=460, y=257)

        bt = Button(self.five, text="Next", command=self.next23, font=("Bookman Old Style", 11, "bold"), bg="darkblue",
                    fg="white",
                    relief="raised", bd=5)
        bt.place(x=440, y=330)






        self.six = Toplevel()
        self.six.geometry("900x650")
        self.six.configure(background="#9FC6CB")
        self.six.withdraw()
        canvas345 = Canvas(self.six, width=150, height=150, border=0.5, bg="darkgrey", relief="groove", bd=5)
        canvas345.configure(border=0.5)
        canvas345.place(x=20, y=50)
        self.six.my_image = PhotoImage(file='C:\\Users\\hp\\Desktop\\PI.png')
        canvas345.create_image(0, 0, anchor="nw", image=self.six.my_image)

        self.ptilte = Label(self.six, text="              STUDENT DETAILS DATABASE           ", bg="#DBE7FF",
                            font=('Imprint MT Shadow', 13, "bold"),
                            fg="navyblue", relief="groove").pack()
        Label(self.six, text="Department Of Computer Science & Engineering", font=("Imprint MT Shadow ", 16, "bold"),
              fg="maroon", bg="#F5FFCF").pack()
        Label(self.six, text="CIE AVG", font=("Bookman Old Style", 15, "bold"), fg="darkgreen").place(x=395, y=95)
        Label(self.six, text="SIE", font=("Bookman Old Style", 15, "bold"), fg="darkgreen").place(x=670, y=95)
        la1 = Label(self.six, text="SUB1:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la1.place(x=280, y=145)
        e1 = Entry(self.six, textvariable=self.sub111, bg="#F4FCE3", font=("Bookman Old Style", 11, "bold"),
                   relief="sunken", bd=4,
                   fg="red", justify="center")
        e1.place(x=350, y=145)
        la2 = Label(self.six, text="SUB2:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la2.place(x=280, y=180)
        e2 = Entry(self.six, textvariable=self.sub222, bg="#F4FCE3", font=("Bookman Old Style", 11, "bold"),
                   relief="sunken", bd=4,
                   fg="red", justify="center")
        e2.place(x=350, y=180)
        la3 = Label(self.six, text="SUB3:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la3.place(x=280, y=215)
        e3 = Entry(self.six, textvariable=self.sub333, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                   bg="#F4FCE3",
                   fg="red", justify="center")
        e3.place(x=350, y=215)
        la4 = Label(self.six, text="SUB4:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la4.place(x=280, y=250)
        e4 = Entry(self.six, textvariable=self.sub444, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                   bg="#F4FCE3",
                   fg="red", justify="center")
        e4.place(x=350, y=250)
        la5 = Label(self.six, text="SUB5:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la5.place(x=280, y=285)
        e5 = Entry(self.six, textvariable=self.sub555, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                   bg="#F4FCE3",
                   fg="red", justify="center")
        e5.place(x=350, y=285)
        la6 = Label(self.six, text="SUB6:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la6.place(x=280, y=325)
        e6 = Entry(self.six, textvariable=self.sub666, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                   bg="#F4FCE3",
                   fg="red", justify="center")
        e6.place(x=350, y=325)
        la7 = Label(self.six, text="LAB1:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la7.place(x=280, y=365)
        e33 = Entry(self.six, textvariable=self.sub777, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                    bg="#F4FCE3",
                    fg="red", justify="center")
        e33.place(x=350, y=365)
        la8 = Label(self.six, text="LAB2:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la8.place(x=280, y=400)
        e99 = Entry(self.six, textvariable=self.sub888, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                    bg="#F4FCE3",
                    fg="red", justify="center")
        e99.place(x=350, y=400)
        la9 = Label(self.six, text="PLACEMENT:", bg="#DBE7FF", font=("Bookman Old Style", 12, "bold"), fg="navyblue")
        la9.place(x=215, y=440)
        e66 = Entry(self.six, textvariable=self.sub999, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                    bg="#F4FCE3",
                    fg="red", justify="center")
        e66.place(x=350, y=440)

        e7 = Entry(self.six, textvariable=self.sub1111, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                   bg="#F4FCE3",
                   fg="red", justify="center")
        e7.place(x=580, y=145)
        e8 = Entry(self.six, textvariable=self.sub2222, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                   bg="#F4FCE3",
                   fg="red", justify="center")
        e8.place(x=580, y=180)
        e = Entry(self.six, textvariable=self.sub3333, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                  bg="#F4FCE3",
                  fg="red", justify="center")
        e.place(x=580, y=215)
        e9 = Entry(self.six, textvariable=self.sub4444, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                   bg="#F4FCE3",
                   fg="red", justify="center")
        e9.place(x=580, y=250)
        e10 = Entry(self.six, textvariable=self.sub5555, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                    bg="#F4FCE3",
                    fg="red", justify="center")
        e10.place(x=580, y=285)
        e11 = Entry(self.six, textvariable=self.sub6666, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                    bg="#F4FCE3",
                    fg="red", justify="center")
        e11.place(x=580, y=325)
        e12 = Entry(self.six, textvariable=self.sub7777, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                    bg="#F4FCE3",
                    fg="red", justify="center")
        e12.place(x=580, y=365)
        e13 = Entry(self.six, textvariable=self.sub8888, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                    bg="#F4FCE3",
                    fg="red", justify="center")
        e13.place(x=580, y=400)
        e22 = Entry(self.six, textvariable=self.sub9999, font=("Bookman Old Style", 11, "bold"), relief="sunken", bd=4,
                    bg="#F4FCE3",
                    fg="red", justify="center")
        e22.place(x=580, y=440)
        bt = Button(self.six, text="ADD", command=self.add1, font=("Bookman Old Style", 11, "bold"), bg="darkblue",
                    fg="white",
                    relief="raised", bd=5)
        bt.place(x=440, y=480)

        bt1 = Button(self.six, text="CLOSE", command=self.endprg13, font=("Bookman Old Style", 11, "bold"),
                     bg="darkblue",
                     relief="raised", bd=5,
                     fg="white")
        bt1.place(x=510, y=480)
        bt1 = Button(self.six, text="BACK", command=self.back45, font=("Bookman Old Style", 11, "bold"),
                     bg="darkblue",
                     relief="raised", bd=5,
                     fg="white")
        bt1.place(x=600, y=480)



    def add1(self):
        self.gh=sqlite3.connect("ADMIN.db")
        self.cc=self.gh.cursor()
        self.cc.execute("INSERT INTO INF(NAME,USN,SEMISTER,DEPARTMENT,GPA,EFFICIENCY,IMP_AREA,SUB1,SUB2,SUB3,SUB4,SUB5,SUB6,SUB7,SUB8,SUB9,ATTENDANCE,BACKLOG) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                  (self.usernam11.get(), self.usn12.get(),self.sem1.get(),self.dept1.get(),self.grp1.get(),self.eff1.get(),self.impy1.get(),self.attt.get(),self.bakk.get(),
                   self.sub111.get(), self.sub222.get(), self.sub333.get(), self.sub444.get(), self.sub555.get(), self.sub666.get(),
                   self.sub777.get(), self.sub888.get(), self.sub999.get()))
        self.cc.execute("INSERT INTO c1(NAME,USN,SUB1,SUB2,SUB3,SUB4,SUB5,SUB6,LAB1,LAB2,PLMNT) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
            (self.usernam11.get(), self.usn12.get(),
             self.sub1111.get(), self.sub2222.get(), self.sub3333.get(), self.sub4444.get(), self.sub5555.get(), self.sub6666.get(),
             self.sub7777.get(), self.sub8888.get(), self.sub9999.get()))
        self.cc.execute("INSERT INTO stuff(NAME,USN) VALUES(?,?)",(self.usernam11.get(),self.usn12.get()))
        self.gh.commit()

        messagebox.showinfo("STUDENT ENTRY", "SUCCESSFULLY ADDED")
        self.clear1()

    def clear1(self):
        self.usernam11.set('')
        self.usn12.set('')
        self.dept1.set('')
        self.grp1.set('')
        self.sem1.set('')
        self.impy1.set('')
        self.attt.set('')
        self.bakk.set('')
        self.eff1.set('')
        self.sub111.set('')
        self.sub222.set('')
        self.sub333.set('')
        self.sub444.set('')
        self.sub555.set('')
        self.sub666.set('')
        self.sub777.set('')
        self.sub888.set('')
        self.sub999.set('')
        self.sub1111.set('')
        self.sub2222.set('')
        self.sub3333.set('')
        self.sub4444.set('')
        self.sub5555.set('')
        self.sub6666.set('')
        self.sub7777.set('')
        self.sub8888.set('')
        self.sub9999.set('')

    def back45(self):
        self.six.withdraw()
        self.second.deiconify()

    def next23(self):
        self.five.withdraw()
        self.six.deiconify()

    def endprg13(self):
        self.six.destroy()
        self.five.destroy()
        self.master.destroy()
    def add(self):
        self.second.withdraw()
        self.five.deiconify()


    def endprg15(self):
        self.four.destroy()
        self.third.destroy()
        self.second.destroy()
        self.master.destroy()

    def back(self):
        self.four.withdraw()
        self.third.deiconify()
        self.second.withdraw()

    def back1(self):
        self.third.withdraw()
        self.second.deiconify()
        self.four.withdraw()
        self.master.withdraw()
    def endprg6(self):
        self.master.destroy()
    def endprg11(self):
        self.second.destroy()
        self.master.destroy()

    def endprg1(self):
        self.third.destroy()
        self.second.destroy()
        self.master.destroy()
    def endprg12(self):
        self.four.destroy()
        self.third.destroy()
        self.second.destroy()
        self.master.destroy()
    def next(self):
        self.second.withdraw()
        self.third.withdraw()
        self.four.deiconify()

    def login(self):
        self.db = sqlite3.connect("ADMIN.db")
        self.c = self.db.cursor()
        self.sql = "SELECT * FROM stuff WHERE USN=? AND NAME=?"
        self.c.execute(self.sql, [(self.usn.get()),(self.username.get())])
        self.row = self.c.fetchone()
        if self.row:
            self.cer = "SELECT * FROM INF WHERE USN=? AND NAME=?"
            self.c.execute(self.cer, [(self.usn.get()),(self.username.get())])
            self.row1 = self.c.fetchone()
            if self.row1:
                messagebox.showinfo("WELCOME", "Record Found")
                self.usernam1.set(self.row1[0])
                self.usn1.set(self.row1[1])
                self.sem.set(self.row1[2])
                self.dept.set(self.row1[3])
                self.grp.set(self.row1[4])
                self.eff.set(self.row1[5])
                self.impy.set(self.row1[6])

                self.sub1.set(self.row1[7])
                self.sub2.set(self.row1[8])
                self.sub3.set(self.row1[9])
                self.sub4.set(self.row1[10])
                self.sub5.set(self.row1[11])
                self.sub6.set(self.row1[12])
                self.sub7.set(self.row1[13])
                self.sub8.set(self.row1[14])
                self.sub9.set(self.row1[15])
                self.att.set((self.row1[16]))
                self.bak.set(self.row1[17])
                self.cer = "SELECT * FROM c1 WHERE USN=? AND NAME=?"
                self.c.execute(self.cer, [(self.usn.get()),(self.username.get())])
                self.row11 = self.c.fetchone()
                if self.row11:
                    self.sub11.set(self.row11[2])
                    self.sub22.set(self.row11[3])
                    self.sub33.set(self.row11[4])
                    self.sub44.set(self.row11[5])
                    self.sub55.set(self.row11[6])
                    self.sub66.set(self.row11[7])
                    self.sub77.set(self.row11[8])
                    self.sub88.set(self.row11[9])
                    self.sub99.set(self.row11[10])


                else:
                    messagebox.showerror()
                    self.clear()
                self.second.withdraw()
                self.third.deiconify()
                self.clear()
            else:
                messagebox.showerror("ERROR", "Record Not Found\n Or\n Please Input Correct Name And USN")
                self.clear()


        else:
            messagebox.showerror("ERROR", "Record Not Found\n Or\n Please Input Correct Name And USN")
            self.clear()


    def clear(self):
        self.usn.set('')
        self.username.set('')
        self.uname.set('')
        self.passw3.set('')

    def endprg2(self):
        self.third.destroy()
        self.second.destroy()
        self.master.destroy()
    def login1(self):
        self.db = sqlite3.connect("ADMIN.db")
        self.c = self.db.cursor()
        self.sql = "SELECT * FROM login WHERE USER=? AND PASS=?"
        self.c.execute(self.sql, [(self.uname.get()), (self.passw3.get())])
        self.row = self.c.fetchone()
        if self.row:
            messagebox.showinfo("WELOCME","Login Successfull")
            self.master.withdraw()
            self.second.deiconify()
        else:
            messagebox.showerror("ERROR", "Record Not Found\n Or\n Please Input Correct Username And Password")
            self.clear()



mw = Tk()
mw.geometry("600x350")
mw.configure(background="darkgrey",border=0.5)
mw.title("COMPUTER SCIENCE DEPARTMENT")
myapp = window(mw)
mw.mainloop()
