from tkinter import *
import mysql.connector as sc
import datetime
day=int(input("Date of DOB"))
mo=int(input("Month of DOB "))
yr=int(input('Year of DOB'))
DOB1=datetime.date(yr,mo,day)



root = Tk()

def getvals():
    sn = nameentry.get()
    fn = fnameentry.get()
    mn = mnameentry.get() 
    ge = genderentry.get()
    cn = snameentry.get()
    dob = DOB1 
    
    conn=sc.connect(host='localhost',user='root',password='123456',database='project',charset='utf8')
    cur=conn.cursor()
    savedata="insert into reg2(StName, FName, MName, Gender, Sname ,dob) values(%s, %s, %s, %s, %s, %s)"
    val = (sn, fn, mn, ge, cn, dob)
    cur.execute(savedata,val)
    conn.commit()
    print('Record Saved Successfuly') 
    conn.close()
    
    

def RollNum():
    
    sn = nameentry.get() 
    cn = snameentry.get()
    conn=sc.connect(host='localhost',user='root',password='123456',database='project',charset='utf8')
    cur=conn.cursor()
    str1="Select RollNo from reg2 where StName='"+sn+"' and SName= '"+cn+"'"
    cur.execute(str1)
    data=cur.fetchall()
    for r in data:
        print(r)  
    conn.close() 
    

root.geometry("400x400")
root.minsize(300,300)
root.maxsize(330,330)

root.title("IP PROJECT")

Label(root, text="Exam Registration Portal", font="BreeSerif 10 bold", pady=10).grid(row=0, column=3)

#Text for our form
name = Label(root, text="Students Full Name", fg="red")
fname = Label(root, text="Fathers Name", fg="red")
mname = Label(root, text="Mothers Name", fg="red")
gender = Label(root, text="Gender", fg="red")
sname = Label(root, text="School Name", fg="red")
#dob = Label(root, text="Date of Birth(YYYY-MM-DD)", fg="red")


#Pack text for our form
name.grid(row=1, column=2)
fname.grid(row=2, column=2)
mname.grid(row=3, column=2)
gender.grid(row=4, column=2)
sname.grid(row=5,column=2) 
#dob.grid(row=6,column=2)


# Tkinter variable for storing entries
namevalue = StringVar()
fnamevalue = StringVar()
mnamevalue = StringVar()
gendervalue = StringVar()
snamevalue = StringVar()
#dobvalue = StringVar()


#Entries for our form
nameentry = Entry(root, textvariable=namevalue)
fnameentry = Entry(root, textvariable=fnamevalue)
mnameentry = Entry(root, textvariable=mnamevalue)
genderentry = Entry(root, textvariable=gendervalue)
snameentry = Entry(root, textvariable=snamevalue)
#dobentry = Entry(root, textvariable=dobvalue)

# Packing the Entries
nameentry.grid(row=1, column=3)
fnameentry.grid(row=2, column=3)
mnameentry.grid(row=3, column=3)
genderentry.grid(row=4, column=3)
snameentry.grid(row=5, column=3)
#dobentry.grid(row=6, column=3)

#Button & packing it and assigning it a command
Button(text="Submit the form", command=getvals).grid(row=7, column=3, pady=5) 
Button(text="Get your Roll Number", command=RollNum).grid(row=8, column=3, pady=5) 


root.mainloop()