from tkinter import *

top = Tk()
top.geometry("600x375")

Custid = Label(top, text="Custid").place(x=40, y=60)

Custid_entry = Entry(top, width=30).place(x=150, y=60)


Name = Label(top, text="Customer Name").place(x=40, y=90)
Name_entry = Entry(top, width=30).place(x=150, y=90)

Branch = Label(top, text="Branch").place(x=40, y=120)
Branch_entry = Entry(top, width=30).place(x=150, y=120)

Account_type = Label(top, text="Account type").place(x=40, y=150)
var = IntVar()
Saving = Radiobutton(top, text="Saving", variable=var, value=1).place(x=150, y=150)
Non_saving = Radiobutton(top, text="Non Saving", variable=var, value=2).place(
    x=250, y=150
)

Amount = Label(top, text="Amount").place(x=40, y=180)
scale = Scale(top, variable=var, orient=HORIZONTAL).place(x=100, y=180)

Insert = Button(top, text="Insert").place(x=40, y=220)
Insert = Button(top, text="Update").place(x=120, y=220)
Insert = Button(top, text="Delete").place(x=40, y=260)
Insert = Button(top, text="Select").place(x=120, y=260)
top.mainloop()
