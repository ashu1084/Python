from tkinter import *

root = Tk()
root.geometry("800x500")

root.title("Flyer")

Bookingid = Label(root, text="Bookingid", font="Helvetica 10 bold").place(x=10, y=10)

bookingIdEntry = Entry(root, width=30).place(x=140, y=10)


passengerName = Label(root, text="Passenger Name", font="Helvetica 10 bold").place(
    x=10, y=40
)
passengerNameEntry = Entry(root, width=30).place(x=140, y=40)


flight = Label(root, text="Flight", font="Helvetica 10 bold").place(x=10, y=70)
fligtEntry = Entry(root, width=30).place(x=140, y=70)

source = Label(root, text="Source", font="Helvetica 10 bold").place(x=10, y=110)
delhi = Radiobutton(text="Delhi", font="Helvetica 10 bold").place(x=140, y=110)
mumbaiDestination = Radiobutton(
    root, text="Mumbai Destination", font="Helvetica 10 bold"
).place(x=300, y=110)
chennai = Radiobutton(root, text="Chennai", font="Helvetica 10 bold").place(
    x=500, y=110
)
chennai = Radiobutton(root, text="Kolkata", font="Helvetiaca 10 bold").place(
    x=650, y=110
)

duration = Label(root, text="Duration", font="Helvetica 10 bold").place(x=10, y=140)
durationSpinBox = Spinbox(root, width=30, from_=1, to=20).place(x=140, y=140)

insert = Button(root, text="Insert", font="Helvetica 10 bold").place(x=10, y=170)
update = Button(root, text="Update", font="Helvetica 10 bold").place(x=110, y=170)
delete = Button(root, text="Delete", font="Helvetica 10 bold").place(x=10, y=210)
select = Button(root, text="Select", font="Helvetica 10 bold").place(x=110, y=210)


root.mainloop()
