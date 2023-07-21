import mysql.connector as sqlcon


sn = int(input('Enter your Roll Number : '))
dob=input("Enter your DOB(in yyyy-mm-dd)")



con=sqlcon.connect(host='localhost',user='root',password='1234', database='project',charset='utf8')
mycur=con.cursor()
str1="Select StName from reg2 where RollNo = '"+str(sn)+"' & dob= '"+str(dob)+"' "
mycur.execute(str1)
data1=mycur.fetchall()
print(data1)
con.close()
   
con=sqlcon.connect(host='localhost',user='root',password='1234', database='project',charset='utf8')
mycur=con.cursor() 
strf="Select FName from reg2 where RollNo = '"+str(sn)+"'  & dob= '"+str(dob)+"' "
mycur.execute(strf)
data=mycur.fetchall()
print(data)
con.close() 

con=sqlcon.connect(host='localhost',user='root',password='1234', database='project',charset='utf8')
mycur=con.cursor() 
strm="Select MName from reg2 where RollNo = '"+str(sn)+"' & dob= '"+str(dob)+"' "
mycur.execute(strm)
data2=mycur.fetchall()
print(data2)
con.close() 

con=sqlcon.connect(host='localhost',user='root',password='1234', database='project',charset='utf8')
mycur=con.cursor() 
strg="Select Gender from reg2 where RollNo = '"+str(sn)+"' & dob= '"+str(dob)+"' "
mycur.execute(strg)
data3=mycur.fetchall()
print(data3)
con.close() 

con=sqlcon.connect(host='localhost',user='root',password='1234', database='project',charset='utf8')
mycur=con.cursor() 
strsn="Select SName from reg2 where RollNo = '"+str(sn)+"' & dob= '"+str(dob)+"' "
mycur.execute(strsn)
data4=mycur.fetchall()
print(data4)
con.close() 

con=sqlcon.connect(host='localhost',user='root',password='1234', database='project',charset='utf8')
mycur=con.cursor() 
date="Select DOB from reg2 where RollNo = '"+str(sn)+"' & dob= '"+str(dob)+"' "
mycur.execute(date)
data5=mycur.fetchall()
print(data5)
con.close() 



from tkinter import *
ticket = Tk()
ticket.title("Hall Ticket") 

ticket.geometry("300x300")

Label(ticket, text="XYZ Exam Hall Ticket", font="BreeSerif 10 bold", padx=50, pady=7).place(x=60, y=10)
name = Label(ticket, text="Students Full Name", fg="red")

fname = Label(ticket, text="Fathers Name", fg="red")
mname = Label(ticket, text="Mothers Name", fg="red")
gender = Label(ticket, text="Gender", fg="red")
sname = Label(ticket, text="School Name", fg="red") 
dob = Label(ticket, text="Date of Birth", fg="red") 

name.place(x=10, y=40)

fname.place(x=10, y=80)
mname.place(x=10, y=120)
gender.place(x=10, y=160)
sname.place(x=10, y=200)
dob.place(x=10, y=240)


nameentry = Label(ticket, text=str1)
fnameentry = Label(ticket, text=str)
mnameentry = Label(ticket, text=data2)
genderentry = Label(ticket, text=data3)
snameentry = Label(ticket, text=data4)
dobentry = Label(ticket, text=data5)


nameentry.place(x=140, y=40)

fnameentry.place(x=140, y=80)
mnameentry.place(x=140, y=120)
genderentry.place(x=140, y=160)
snameentry.place(x=140, y=200)
dobentry.place(x=140, y=240)





ticket.mainloop()
