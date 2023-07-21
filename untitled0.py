from tkinter import *     
ticket = Tk()
ticket.title("Hello world")

ticket.geometry("300x300")

Label(ticket, text="Hello",font="BreeSerif 10 bold", padx=50, pady=7).place(x=50,y=10)
name= Label(ticket, text="Students Full Name", fg="red")

name.place(x=10, y=40)

#nameentry = Label(ticket, text=str)

#nameentry.place(x=140, y=40)

button = Button(text="Button 1")
button.place(x=10,y=80)

ticket.mainloop()

