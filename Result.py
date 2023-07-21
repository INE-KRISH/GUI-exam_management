import mysql.connector as sqlcon
import datetime
sn = int(input('Enter your Roll Number : '))
DOB=input("What is your Date of Birth? (in YYYY/MM/dd) ")
DOB1=datetime. datetime. strptime(DOB,"%Y-%m-%d"). date()
dob=DOB1


con=sqlcon.connect(host='localhost',user='root',password='1234', database='project',charset='utf8')
mycur=con.cursor()
str1="Select StName from reg2 where RollNo = '"+str(sn)+"' & dob= '"+str(dob)+"' "
mycur.execute(str1)
data=mycur.fetchall()
for r in data:
    print(r)
con.close()
   
con=sqlcon.connect(host='localhost',user='root',password='1234', database='project',charset='utf8')
mycur=con.cursor() 
strf="Select FName from reg2 where RollNo = '"+str(sn)+"' & dob= '"+str(dob)+"' "
mycur.execute(strf)
data=mycur.fetchall()
for f in data:
    print(f)
con.close() 

con=sqlcon.connect(host='localhost',user='root',password='1234', database='project',charset='utf8')
mycur=con.cursor() 
strm="Select MName from reg2 where RollNo = '"+str(sn)+"' & dob= '"+str(dob)+"' "
mycur.execute(strm)
data=mycur.fetchall()
for m in data:
    print(m)
con.close() 

con=sqlcon.connect(host='localhost',user='root',password='1234', database='project',charset='utf8')
mycur=con.cursor() 
strg="Select Gender from reg2 where RollNo = '"+str(sn)+"' & dob= '"+str(dob)+"' "
mycur.execute(strg)
data=mycur.fetchall()
for g in data:
    print(g)
con.close() 

con=sqlcon.connect(host='localhost',user='root',password='1234', database='project',charset='utf8')
mycur=con.cursor() 
strsn="Select SName from reg2 where RollNo = '"+str(sn)+"' & dob= '"+str(dob)+"' "
mycur.execute(strsn)
data=mycur.fetchall()
for sn in data:
    print(sn)
con.close() 

con=sqlcon.connect(host='localhost',user='root',password='1234', database='project',charset='utf8')
mycur=con.cursor() 
date="Select DOB from reg2 where RollNo = '"+str(sn)+"' & dob= '"+str(dob)+"' "
mycur.execute(date)
data=mycur.fetchall()
for do in data:
    print(do)
con.close()









from tkinter import *
ticket = Tk()
ticket.title("Result") 

ticket.geometry("1260x860")

Label(ticket, text="RESULT OF XYZ-ABC", font="BreeSerif 10 bold", padx=1, pady=1).place(x=50, y=10)
name = Label(ticket, text="Students Full Name", fg="green")
fname = Label(ticket, text="Fathers Name", fg="green")
mname = Label(ticket, text="Mothers Name", fg="green")
gender = Label(ticket, text="Gender", fg="green")
sname = Label(ticket, text="School Name", fg="green")


name.place(x=10, y=40)
fname.place(x=10, y=80)
mname.place(x=10, y=120)
gender.place(x=10, y=160)
sname.place(x=10, y=200)


nameentry = Label(ticket, text=r)
fnameentry = Label(ticket, text=f)
mnameentry = Label(ticket, text=m)
genderentry = Label(ticket, text=g)
snameentry = Label(ticket, text=sn)
dobentry = Label(ticket, date=do)

ticket.mainloop()
