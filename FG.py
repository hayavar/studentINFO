from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3


class app(tk.Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (startpage, pageone):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(startpage)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()


class startpage(Frame):
    def __init__(self, parent, controlleer):
        Frame.__init__(self, parent)
        label = Label(self, text="username")
        label.pack(padx=10, pady=10)
        e1=Entry(self,textvariable=self)
        e1.pack()
        label1 = Label(self, text="password")
        label1.pack(padx=10, pady=10)
        e2 = Entry(self, textvariable=controlleer, show='*')
        e2.pack()
        page_one = Button(self, text="page one", command=lambda: controlleer.show_frame(pageone))
        page_one.pack()
       

class pageone(Frame):
    def __init__(self, parent, controlleer):
        Frame.__init__(self, parent)
        self.controlleer = controlleer
        self.name2 = StringVar
        self.usn = StringVar
        self.sem = StringVar
        self.dept = StringVar
        self.gpa = StringVar
        self.eff = StringVar
        self.impy = StringVar
        label = Label(self, text="STUDENT INFORMATION")
        label.pack(padx=10, pady=10)
        label.place(x=600, y=10)
        self.db = sqlite3.connect("STDLOGIN.db")
        self.c = self.db.cursor()
        self.c.execute("SELECT * FROM INF")
        self.t=self.c.fetchone()




        canvas = Canvas(self, width=100, height=100,border=0.5,bg="green")
        canvas.configure(border=0.5)
        canvas.place(x=300, y=50)
        self.my_image = PhotoImage(file='C:\\Users\\hp\\Downloads\\kl.png')
        canvas.create_image(0, 0, anchor="nw", image=self.my_image)
        l3 = Label(self, text="NAME:", fg="BLUE", font=(None, 9, "bold"), bg="white")
        e3 = Entry(self, textvariable=self.name2, fg="RED", bg="white")
        l4 = Label(self, text="USN:", fg="BLUE", font=(None, 9, "bold"), bg="white")
        e4 = Entry(self, textvariable=self.usn, fg="RED")
        l5 = Label(self, text="SEM:", fg="GREEN", font=(None, 9, "bold"), bg="white")
        e5 = Entry(self, textvariable=self.sem, fg="RED")
        l6 = Label(self, text="DEPT:", fg="GREEN", font=(None, 9, "bold"), bg="white")
        e6 = Entry(self, textvariable=self.dept, fg="RED")
        l7 = Label(self, text="GPA:", fg="GREEN", font=(None, 9, "bold"), bg="white")
        e7 = Entry(self, textvariable=self.gpa, fg="RED")
        l8 = Label(self, text="EFFNCY(%):", fg="GREEN", font=(None, 10, "bold"), bg="white")
        e8 = Entry(self, textvariable=self.eff, fg="RED")
        l9 = Label(self, text="IMPT_AREA:", fg="GREEN", font=(None, 10, "bold"), bg="white")
        e9 = Entry(self, textvariable=self.impy, fg="RED")
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






def main():
    bpp = app()
    bpp.mainloop()


if __name__ == '__main__':
    main()
