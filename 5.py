from tkinter import *

root = Tk()
root.geometry("800x500")

root.title("Movie Ticet Booking")

movieBookingid = Label(root, text="Movie Bookingid", font="Helvetica 10 bold").place(
    x=10, y=10
)

movieBookingIdEntry = Entry(root, width=30).place(x=140, y=10)


personName = Label(root, text="Person Name", font="Helvetica 10 bold").place(x=10, y=40)
personNameEntry = Entry(root, width=30).place(x=140, y=40)


movieName = Label(root, text="Movie Name", font="Helvetica 10 bold").place(x=10, y=70)
movieNameEntry = Entry(root, width=30).place(x=140, y=70)

classLabel = Label(root, text="Class", font="Helvetica 10 bold").place(x=10, y=110)
a = Radiobutton(text="A", font="Helvetica 10 bold").place(x=140, y=110)
b = Radiobutton(root, text="B", font="Helvetica 10 bold").place(x=250, y=110)

timeOfShow = Label(root, text="Time of Show", font="Helvetica 10 bold").place(
    x=350, y=110
)
evening = Checkbutton(root, text="7:15 pm", font="Helvetica 10 bold").place(
    x=500, y=110
)
morining = Checkbutton(root, text="9 am", font="Helvetiaca 10 bold").place(x=650, y=110)

noOfTickets = Label(root, text="No of Tickets", font="Helvetica 10 bold").place(
    x=10, y=150
)
noOfTicketsScale = Scale(root, orient=HORIZONTAL).place(x=140, y=140)
insert = Button(root, text="Insert", font="Helvetica 10 bold").place(x=10, y=200)
update = Button(root, text="Update", font="Helvetica 10 bold").place(x=110, y=200)
delete = Button(root, text="Delete", font="Helvetica 10 bold").place(x=10, y=230)
select = Button(root, text="Select", font="Helvetica 10 bold").place(x=110, y=230)


root.mainloop()
