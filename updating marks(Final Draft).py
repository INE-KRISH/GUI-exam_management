# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 20:25:46 2022

@author: Admin
"""



from tkinter import *
import mysql.connector as sqlcon
import datetime
import numpy as np
root = Tk()

def getvals():

    en = englishentry.get()
    ma = mathsentry.get()
    ph = physicsentry.get() 
    ch = chemistryentry.get()
    ip = ipentry.get()
    conn=sqlcon.connect(host='localhost',user='root',password='1234',database='project',charset='utf8')
    cur=conn.cursor()
    savedata="insert into Marks1(English, Maths, Physics, Chemistry, IP) values(%s, %s, %s, %s, %s)"
    val = (en,ma,ph,ch,ip)
    cur.execute(savedata,val)
    conn.commit()
    print('Record Saved Successfuly') 
    conn.close()
def marks():   
                    root.geometry("400x400")
                    root.minsize(330,330)
                    root.maxsize(360,360)
                    
                    root.title("IP PROJECT")
                    
                    Label(root, text="Exam Registration Portal", font="BreeSerif 10 bold", pady=10).pack()
                        
                    
                    rol = Label(root, text="Roll No.", fg="red")
                    dob = Label(root, text="Date of birth", fg="red")
                    english = Label(root, text="English", fg="red")
                    maths = Label(root, text="Maths", fg="red")
                    physics = Label(root, text="Physics", fg="red")
                    chemistry = Label(root, text="chemistry", fg="red")
                    ip = Label(root, text="IP", fg="red")
                    
                    rol.pack()
                    rolvalue = int()
                    rolentry = Entry(root)
                    rolentry.pack()
                    
                    dob.pack()
                    dobvalue = int()
                    dobentry = Entry(root)
                    dobentry.pack()
                    
                    english.pack()
                    englishvalue = int()
                    englishentry = Entry(root)
                    englishentry.pack()
                    
                    maths.pack()
                    mathsvalue = int()
                    mathsentry = Entry(root)
                    mathsentry.pack()
    
                    physics.pack()
                    physicsvalue = int()
                    physicsentry = Entry(root)
                    physicsentry.pack()

                    chemistry.pack()
                    chemistryvalue = int()
                    chemistryentry = Entry(root)
                    chemistryentry.pack()
                    
                    ip.pack()
                    ipvalue = int()
                    ipentry = Entry(root)
                    ipentry.pack()       

                    
                    
                    Button(text="Submit the marks", command=getvals).pack()
                    
                    root.mainloop()

x=0

if x==0:
    con=sqlcon.connect(host='localhost',user='root',password='1234', database='project',charset='utf8')
    mycur=con.cursor() 
    x=input('Enter the username:')
    str2 = "Select username from T_ID where username = '"+str(x)+"'" 
    mycur.execute(str2)
    data=mycur.fetchall()
    for g in data:
        y=g
        print('username is correct')

con.close() 
   
    


if y!=0:
   
        con=sqlcon.connect(host='localhost',user='root',password='1234', database='project',charset='utf8')
        mycur=con.cursor() 
        x=input('Enter the password:')
        
        str2 = "Select PASSWORD from T_ID where password = '"+str(x)+"'" 
        mycur.execute(str2)
        
        data=mycur.fetchall()
        for g in data:
            h=g
            print('Password is correct')
        con.close()
            
        if h!=0:
            print('Access Granted:')
            marks()       
          