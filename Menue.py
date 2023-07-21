from tkinter import *
from tkinter import messagebox

menue = Tk()

def reg():
    import untitled4
    untitled4.mainloop()
    
def ht():
    import AdmitCard
    AdmitCard.mainloop()

def res():
    messagebox.showinfo("Result","You have been promoted to the next class")






menue.title("MENUE")

menue.geometry("350x150")
menue.minsize(350,150)
menue.maxsize(350,150)

Label(menue, text="..........MENU..........", font="BreeSerif 20 bold", fg="magenta", pady=4).pack(side=TOP)
Label(menue, text="Select your choice", font="BreeSerif 16", fg="indigo", pady=2).pack(side=TOP)

frame = Frame(menue, borderwidth=5, bg="orange", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw", padx=45)

b1 = Button(frame, fg="red", text="Exam Registration", command=reg) 
b1.pack(side=LEFT, padx=5, pady=5)

b2 = Button(frame, fg="blue", text="Hall Ticket", command=ht) 
b2.pack(side=LEFT, padx=5, pady=5)

b3 = Button(frame, fg="green", text="Result", command=res) 
b3.pack(side=LEFT, padx=5, pady=5)

menue.mainloop()