# -*- coding: utf-8 -*-
"""
@author: Souradeep Mondal

Created on Mon Apr 20 15:41:45 2021

Project on Online Exam Management
MODULE : Online Exam Management

NOTE: database read write not work
"""

import tkinter as tk
import sqlite3
from sqlite3 import Error
from tkinter import *
from tkinter.ttk import *
import os
import platform

path="test.db"

# def combine_funcs(*funcs):
#     def combined_func(*args, **kwargs):
#         for f in funcs:
#             f(*args, **kwargs)
#     return combined_func

def clrscreen():
    if platform.system() == "Windows":
        print(os.system("cls"))
        
        
# def DatabaseCreate():
#     cnx = sqlite3.connect(path)
#     Cursor = cnx.cursor()
#     Cursor.execute("CREATE DATABASE IF NOT EXISTS online_exam;")
#     Cursor.execute("")
#     Cursor.close()
#     cnx.close()


def TablesCreate():
    cnx = sqlite3.connect(path)
    Cursor = cnx.cursor()
    Cursor.execute("""CREATE TABLE IF NOT EXISTS Student (User_ID text PRIMARY KEY, Password text, Email_Address text, Name text, Roll_Number text, Phone number)""")
    print(Cursor.fetchone())
    if Cursor.fetchone() == 1:
        print("1 go")
    else:
        print("1 no go")
    Cursor.execute("""CREATE TABLE IF NOT EXISTS Subject (Subject_ID text PRIMARY KEY, Subject_name text, Credits integer, Teacher text);""")
    print(Cursor.fetchone())
    if Cursor.fetchone() == 1:
        print("2 go")
    else:
        print("2 no go")
    Cursor.execute("""CREATE TABLE IF NOT EXISTS Exam (Exam_ID text PRIMARY KEY, User_ID text, Subject_ID text, Exam_Link text);""")
    print(Cursor.fetchone())
    if Cursor.fetchone() == 1:
        print("3 go")
    else:
        print("3 no go")
    # Cursor.close()
    # cnx.close()


def MenuStudent():
    window1=tk.Toplevel(root)
    window1.title("Student Record Management")
    astu=tk.Button(window1,text="Add Student", command=insertData)
    ssr1=tk.Button(window1,text="Search Student Record", command=SearchStudentRec)
    dsr1=tk.Button(window1,text="Delete Student Record", command=deleteStudent)
    uur=tk.Button(window1,text="Update Update Record", command=UpdateStudent)
    re1=tk.Button(window1,text="Return to Main Menu", command=window1.destroy)
    # astu.grid(row=0,column=0)
    # ssr1.grid(row=1,column=0)
    # dsr1.grid(row=2,column=0)
    # uur.grid(row=3,column=0)
    # re.grid(row=4,column=0)
    astu.pack()
    ssr1.pack()
    dsr1.pack()
    uur.pack()
    re1.pack()
    canvas1=tk.Canvas(window1)
    canvas1.pack()
    #window1.mainloop()
        
def MenuSubject():
    window2=tk.Toplevel(root)
    window2.title("Subject Record Management")
    asr=tk.Button(window2,text="Add Subject Record", command=insertSubject)
    ssr2=tk.Button(window2,text="Search Subject Record", command=SearchSubject)
    dsr2=tk.Button(window2,text="Delete Subject Record", command=deleteSubject)
    usr2=tk.Button(window2,text="Update Subject Record", command=UpdateSubject)
    re2=tk.Button(window2,text="Return to Main Menu", command=window2.destroy)
    # asr.grid(row=0,column=0)
    # ssr2.grid(row=1,column=0)
    # dsr2.grid(row=2,column=0)
    # usr2.grid(row=3,column=0)
    # re2.grid(row=4,column=0)
    asr.pack()
    ssr2.pack()
    dsr2.pack()
    usr2.pack()
    re2.pack()
    canvas2=tk.Canvas(window2)
    canvas2.pack()
    #window2.mainloop()

def MenuExam():
    root3=tk.Toplevel(root)
    root3.title(" Member Record Management")
    asr=tk.Button(root3,text="Add Exam", command=AddExam)
    ssr3=tk.Button(root3,text="Delete Exam", command=DeleteExam)
    dsr=tk.Button(root3,text="View Exam", command=ViewExam)
    re=tk.Button(root3,text="Return to Main Menu", command=root3.destroy)
    asr.grid(row=0,column=0)
    ssr3.grid(row=1,column=0)
    dsr.grid(row=2,column=0)
    re.grid(row=3,column=0)
    canvas3=tk.Canvas(root3)
    canvas3.pack()
    #root3.mainloop()

def AddExam():
    addexam = tk.Toplevel(root)
    addexam.title("Add Exam")
    e_label = tk.Label(addexam, text = 'Enter Exam_ID :')
    e_label.grid(row=0,column=0)
    Exam_ID  = tk.StringVar() #input("Enter Exam_ID : ")
    e_entry = tk.Entry(addexam, textvariable=Exam_ID)
    e_entry.grid(row=0,column=1)
    
    u_label = tk.Label(addexam, text = 'Enter User_ID :')
    u_label.grid(row=1,column=0)
    User_ID = tk.StringVar()#input("Enter User_ID : ")
    u_entry = tk.Entry(addexam, textvariable=User_ID)
    u_entry.grid(row=1,column=1)
    
    s_label = tk.Label(addexam, text = 'Enter Subject_ID :')
    s_label.grid(row=2,column=0)
    Subject_ID = tk.StringVar()#input("Enter Subject_ID : ")
    s_entry = tk.Entry(addexam, textvariable=Subject_ID)
    s_entry.grid(row=2,column=1)
    
    el_label = tk.Label(addexam, text = 'Enter Exam Link :')
    el_label.grid(row=3,column=0)
    Exam_Link = tk.StringVar()#input("Enter Exam Link : ")
    el_entry = tk.Entry(addexam, textvariable=Exam_Link)
    el_entry.grid(row=3,column=1)
    
    sub_btn=tk.Button(addexam, text = 'Submit', command = lambda:[AddExam2(Exam_ID, User_ID, Subject_ID, Exam_Link),addexam.destroy()])
    sub_btn.grid(row=4)

    canvas4=tk.Canvas(addexam)
    canvas4.pack()
    #addexam.mainloop()


def AddExam2(Exam_ID, User_ID, Subject_ID, Exam_Link):
    cnx = sqlite3.connect(path)
    Cursor = cnx.cursor()
    
    Qry = ("INSERT INTO Exam VALUES (?,?,?,?);")
    data = (Exam_ID, User_ID, Subject_ID, Exam_Link)
    Cursor.execute(Qry,data)
    # cnx.commit()
    # Cursor.close()
    # cnx.close()
    print("Record Inserted.")
    # cnx.close()
    Exam_ID.set("")
    User_ID.set("")
    Subject_ID.set("")
    Exam_Link.set("")

def DeleteExam():
    deleteexam = tk.Toplevel(root)
    deleteexam.title("Delete Exam")
    e_label = tk.Label(deleteexam, text = 'Enter Exam_ID of Exam to be deleted :')
    Exam_ID2  = tk.StringVar() #input("Enter Exam_ID of Exam to be deleted : ")
    e_entry = tk.Entry(deleteexam, textvariable=Exam_ID2)
    sub_btn2=tk.Button(deleteexam,text = 'Submit', command = lambda:[DeleteExam2(Exam_ID2),deleteexam.destroy()])
    e_label.grid(row=0,column=0)
    e_entry.grid(row=0,column=1)
    sub_btn2.grid(row=1,column=0)
    canvas5=tk.Canvas(deleteexam)
    canvas5.pack()
    #deleteexam.mainloop()
    
def DeleteExam2(Exam_ID2):
 	cnx = sqlite3.connect(path)
 	Cursor = cnx.cursor()
 	Exam_ID = Exam_ID2#input("Enter Exam_ID of Exam to be deleted : ")
 	Qry = ("""DELETE FROM Exam WHERE Exam_ID = ?;""")
 	del_rec = (Exam_ID,)
 	Cursor .execute(Qry, del_rec)
# 	cnx.commit()
# 	Cursor.close()
# 	cnx.close()
 	print(Cursor.rowcount, "Record(s) Deleted Successfully.")
#	cnx.close()

def ViewExam():
    viewexam = tk.Toplevel(root)
    viewexam.title("View Exam")
    e_label = tk.Label(viewexam, text = 'Enter Exam_ID of Exam to be searched :')
    Exam_ID3  = tk.StringVar() #input("Enter Exam_ID of Exam to be searched : ")
    e_entry = tk.Entry(viewexam, textvariable=Exam_ID3)
    sub_btn3=tk.Button(viewexam,text = 'Submit', command = lambda:[ViewExam2(Exam_ID3),viewexam.destroy()])
    e_label.grid(row=0,column=0)
    e_entry.grid(row=0,column=1)
    sub_btn3.grid(row=1,column=0)
    canvas6=tk.Canvas(viewexam)
    canvas6.pack()
    #viewexam.mainloop()
    
    
def ViewExam2(Exam_ID3):
    conn = sqlite3.connect(path)
    cnx = conn.cursor()
    query = """SELECT * FROM Exam WHERE Exam_ID = ?;"""
    rec_search = Exam_ID3
    cnx.execute(query,rec_search)
    Rec_count = 0
    dat = cnx.fetchall()
    for (Exam_ID, User_ID,Subject_ID, Exam_Link) in dat:
        Rec_count+=1
        print("=============================================================")
        print("Exam_ID: ", Exam_ID)
        print("User_ID: ", User_ID)
        print("Subject_ID: ", Subject_ID)
        print("Exam_Link: ", Exam_Link)
        print("=============================================================")
# 	    for(Exam_ID, User_ID,Subject_ID, Exam_Link) in Cursor:
# 	        Rec_count += 1
# 	        print("=============================================================")
# 	        print("Exam_ID : ", Exam_ID)
# 	        print("User_ID : ", User_ID)
# 	        print("Subject_ID : ", Subject_ID)
# 	        print("Exam_Link: ", Exam_Link)
# 	        print("=============================================================")
# 	        if Rec_count%2 == 0:
# 	            input("Press any key continue")
# 	            print(Rec_count, "Record(s) found")
# # 	    cnx.commit()
# # 	    Cursor.close()
# # 	    cnx.close()
# 	except Error as err:
#         #print(err)
# 	    cnx.close()
        
def insertData():
    idata = tk.Toplevel(root)
    idata.title("Insert Data")
    uidlabel = tk.Label(idata, text = 'Enter User_ID :')
    uidlabel.grid(row=0,column=0)
    User_ID = tk.StringVar()
    usrid=tk.Entry(idata, textvariable=User_ID)#input("Enter User_ID : ")
    usrid.grid(row=0,column=1)
    
    pwlabel = tk.Label(idata, text = 'Enter Password :')
    pwlabel.grid(row=1,column=0)
    Password = tk.StringVar() #input("Enter Password : ")
    pw = tk.Entry(idata, textvariable=Password)
    pw.grid(row=1,column=1)
        
    ealabel = tk.Label(idata, text = 'Enter Email_Address : ')
    ealabel.grid(row=2,column=0)
    Email_Address = tk.StringVar() #input("Enter Email_Address : ")
    ea = tk.Entry(idata, textvariable=Email_Address)
    ea.grid(row=2,column=1)
        
    nlabel = tk.Label(idata, text = 'Name : ')
    nlabel.grid(row=3,column=0)
    Name = tk.StringVar() # input("Name : ")
    nme = tk.Entry(idata, textvariable=Name)
    nme.grid(row=3,column=1)
        
    rnlabel = tk.Label(idata, text = 'Enter Roll_Number : ')
    rnlabel.grid(row=4,column=0)
    Roll_Number = tk.StringVar() # input("Enter Roll_Number : ")
    rn = tk.Entry(idata, textvariable=Roll_Number)
    rn.grid(row=4,column=1)
        
    plabel = tk.Label(idata, text = 'Enter Phone_Number :  ')
    plabel.grid(row=5,column=0)
    Phone = tk.StringVar() # input("Enter Phone_Number : ")
    pn = tk.Entry(idata, textvariable=Phone)
    pn.grid(row=5,column=1)
        
    button1 = tk.Button(idata,text = 'Submit', command = lambda:[insertData2(User_ID, Password, Email_Address, Name, Roll_Number, Phone),idata.destroy()])
    button1.grid(row=6,column=0)
    canvas7=tk.Canvas(idata)
    canvas7.pack()
    #idata.mainloop()

def insertData2(User_ID, Password, Email_Address, Name, Roll_Number, Phone):
    try:
        
        cnx = sqlite3.connect(path)
        Cursor = cnx.cursor()
        Qry = ("INSERT INTO Student VALUES (?,?,?,?,?,?);")
        data = (User_ID, Password, Email_Address, Name, Roll_Number, Phone)
        Cursor.execute(Qry,data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Record Inserted.")
    except Error as err:
        print(err)
        cnx.close()

def deleteStudent():
    delstu = tk.Toplevel(root)
    delstu.title("Delete Student")
    uidlab = tk.Label(delstu, text = 'Enter User_ID of Student to be deleted :  ')
    uidlab.grid(row=0,column=0)
    User_ID = tk.StringVar()#input("Enter User_ID of Student to be deleted : ")
    uid = tk.Entry(delstu, textvariable=User_ID)
    uid.grid(row=0,column=1)
    button2 = tk.Button(delstu,text = 'Submit', command = lambda:[deleteStudent2(User_ID),delstu.destroy()])
    button2.grid(row=1,column=0)
    canvas8=tk.Canvas(delstu)
    canvas8.pack()
    #delstu.mainloop()

def deleteStudent2(User_ID):
    try:
        
        cnx = sqlite3.connect(path)
        Cursor = cnx.cursor()
        Qry = ("""DELETE FROM Student WHERE User_ID = ?;""")
        del_rec = (User_ID,)
        Cursor .execute(Qry, del_rec)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record(s) Deleted Successfully.")
    except Error as err:
        print(err)
        cnx.close()

def SearchStudentRec():
    ssr = tk.Toplevel(root)
    ssr.title("Search Student record")
    uidlbl = tk.Label(ssr, text = 'Enter User_ID of Student to be searched :  ')
    uidlbl.grid(row=0,column=0)
    User_ID = tk.StringVar()#input("Enter User_ID of Student to be searched : ")
    uid2 = tk.Entry(ssr, textvariable=User_ID)
    uid2.grid(row=0,column=1)
    button2 = tk.Button(ssr,text = 'Submit', command = lambda:[SearchStudentRec2(User_ID),ssr.destroy()])
    button2.grid(row=1,column=0)
    canvas9=tk.Canvas(ssr)
    canvas9.pack()
    #ssr.mainloop()

def SearchStudentRec2(User_ID):
    try:
        
        cnx = sqlite3.connect(path)
        Cursor = cnx.cursor()
        
        query = ("SELECT * FROM Student WHERE User_ID = ?; ")
        rec_srch = (User_ID,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for(User_ID, Password, Email_Address, Name, Roll_Number, Phone) in Cursor:
            Rec_count += 1
            print("=============================================================")
            print("User_ID : ", User_ID)
            print("Password : ", Password)
            print("Email_Address : ", Email_Address)
            print("Name: ", Name)
            print("Roll_Number : ", Roll_Number)
            print("Phone : ", Phone)
            print("=============================================================")
            if Rec_count%2 == 0:
                input("Press any key continue")
                clrscreen()
                print(Rec_count, "Record(s) found")
        cnx.commit()
        Cursor.close()
        cnx.close()
    except Error as err:
        print(err)
        cnx.close()

def UpdateStudent():
    us= tk.Toplevel(root)
    us.title("Update Student")
    uidlabel = tk.Label(us, text = 'Enter User_ID of the Student to be Updated :  ')
    uidlabel.grid(row=0,column=0)
    User_ID = tk.StringVar()#input("Enter User_ID of the Student to be Updated : ")
    uid3 = tk.Entry(us, textvariable=User_ID)
    uid3.grid(row=0,column=1)
    #print("Enter new data")
    nuidlab = tk.Label(us, text = 'Enter User_ID :  ')
    nuidlab.grid(row=1,column=0)
    New_User_ID = tk.StringVar()#input("Enter User_ID : ")
    nuid = tk.Entry(us, textvariable=New_User_ID)
    nuid.grid(row=1,column=1)
        
    pwdlabel = tk.Label(us, text = 'Enter Password : ')
    pwdlabel.grid(row=2,column=0)
    Password = tk.StringVar()#input("Enter Password : ")
    pwd = tk.Entry(us, textvariable=Password)
    pwd.grid(row=2,column=1)
        
    ealabel = tk.Label(us, text = 'Enter Email_Address : ')
    ealabel.grid(row=3,column=0)
    Email_Address = tk.StringVar()#input("Enter Email_Address : ")
    ea = tk.Entry(us, textvariable=Email_Address)
    ea.grid(row=3,column=1)
        
    nmelabel = tk.Label(us, text = 'Name : ')
    nmelabel.grid(row=4,column=0)
    Name = tk.StringVar()#input("Name : ")
    nme = tk.Entry(us, textvariable=Name)
    nme.grid(row=4,column=1)
        
    rnlabel = tk.Label(us, text = 'Enter Roll_Number : ')
    rnlabel.grid(row=5,column=0)
    Roll_Number = tk.StringVar()#input("Enter Roll_Number : ")
    rn = tk.Entry(us, textvariable=Roll_Number)
    rn.grid(row=5,column=1)
        
    plabel = tk.Label(us, text = 'Enter Phone_Number : ')
    plabel.grid(row=6,column=0)
    Phone = tk.StringVar()#input("Enter Phone_Number : ")
    p = tk.Entry(us, textvariable=Phone)
    p.grid(row=6,column=1)
    
    button3 = tk.Button(us,text = 'Submit', command = lambda:[UpdateStudent2(New_User_ID, Password, Email_Address, Name, Roll_Number, Phone, User_ID),us.destroy()])
    button3.grid(row=7,column=0)
    canvas10=tk.Canvas(us)
    canvas10.pack()
    #us.mainloop()
    
def UpdateStudent2(New_User_ID, Password, Email_Address, Name, Roll_Number, Phone, User_ID):
    try:
        
        cnx = sqlite3.connect(path)
        Cursor = cnx.cursor()
        Qry = ("UPDATE Student SET User_ID=?, Password=?, Email_Address=?, Name=?, Roll_Number=?, Phone=? WHERE User_ID  = ?;")
        data = (New_User_ID, Password, Email_Address, Name, Roll_Number, Phone, User_ID)
        Cursor.execute(Qry,data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record(s) Updated Successfully.")
    except Error as err:
        print(err)
        cnx.close()
        
def insertSubject():
    isub = tk.Toplevel(root)
    isub.title("Insert Subject")
    sidlabel = tk.Label(isub, text = 'Enter Subject_ID  :  ')
    sidlabel.grid(row=0,column=0)
    Subject_ID  = tk.StringVar()#input("Enter Subject_ID  : ")
    sid = tk.Entry(isub, textvariable=Subject_ID)
    sid.grid(row=0,column=1)
        
    snlabel = tk.Label(isub, text = 'Enter Subject Name :  ')
    snlabel.grid(row=1,column=0)
    Subject_name = tk.StringVar()#input("Enter Subject Name : ")
    sn = tk.Entry(isub, textvariable=Subject_name)
    sn.grid(row=1,column=1)
        
    credlabel = tk.Label(isub, text = 'Enter Credits :  ')
    credlabel.grid(row=2,column=0)
    Credits = tk.IntVar()#int(input("Enter Credits : "))
    cred = tk.Entry(isub, textvariable=Credits)
    cred.grid(row=2,column=1)
        
    teachlabel = tk.Label(isub, text = 'Enter Teacher Name :  ')
    teachlabel.grid(row=3,column=0)
    Teacher = tk.StringVar()#input("Enter Teacher Name : ")
    teach = tk.Entry(isub, textvariable=Teacher)
    teach.grid(row=3,column=1)
    
    button1 = tk.Button(isub,text = 'Submit', command = lambda:[insertSubject2(Subject_ID,Subject_name, Credits, Teacher),isub.destroy()])
    button1.grid(row=4,column=0)
    canvas11=tk.Canvas(isub)
    canvas11.pack()
    #isub.mainloop()

def insertSubject2(Subject_ID, Subject_name, Credits, Teacher):
    try:
        
        cnx = sqlite3.connect(path)
        Cursor = cnx.cursor()
        
        Qry = ("INSERT INTO Subject VALUES(?,?,?,?);")
        data = (Subject_ID, Subject_name, Credits, Teacher)
        Cursor.execute(Qry, data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Record Inserted.")
    except Error as err:
        print(err)
        cnx.close()

def deleteSubject():
    delsub = tk.Toplevel(root)
    delsub.title("Delete Subject")
    sidlabel = tk.Label(delsub, text = 'Enter Subject_ID to be deleted :  ')
    sidlabel.grid(row=0,column=0)
    Subject_ID = tk.StringVar()#input("Enter Subject_ID to be deleted : ")
    sid = tk.Entry(delsub, textvariable=Subject_ID)
    sid.grid(row=0,column=1)
    button2 = tk.Button(delsub,text = 'Submit', command = lambda:[deleteSubject2(Subject_ID),delsub.destroy()])
    button2.grid(row=1,column=0)
    canvas12=tk.Canvas(delsub)
    canvas12.pack()
    #delsub.mainloop()
    
def deleteSubject2(Subject_ID):
    try:
        
        cnx = sqlite3.connect(path)
        Cursor = cnx.cursor()

        Qry =("""DELETE FROM Subject WHERE Subject_ID = ?;""")
        del_rec = (Subject_ID,)
        Cursor.execute(Qry, del_rec)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record(s) Deleted Successfully.")
    except Error as err:
        print(err)
        cnx.close()

def SearchSubject():
    ss = tk.Toplevel(root)
    ss.title("Search Subject")
    sidlabel = tk.Label(ss, text = 'Enter Subject_ID to be Searched :  ')
    sidlabel.grid(row=0,column=0)
    Subject_ID = tk.StringVar()#input("Enter Subject_ID to be Searched : ")
    sid = tk.Entry(ss, textvariable=Subject_ID)
    sid.grid(row=0,column=1)
    button3 = tk.Button(ss,text = 'Submit', command = lambda:[SearchSubject2(Subject_ID),ss.destroy()])
    button3.grid(row=1,column=0)
    canvas13=tk.Canvas(ss)
    canvas13.pack()
    #ss.mainloop()
    
    
def SearchSubject2(Subject_ID):
    try:
        
        cnx = sqlite3.connect(path)
        Cursor = cnx.cursor()
        
        query = ("SELECT * FROM Subject where Subject_ID = ?;")
        rec_srch = (Subject_ID,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for(Subject_ID,Subject_name, Credits,Teacher) in Cursor:
            Rec_count += 1
            print("=============================================================")
            print("Subject_ID : ", Subject_ID)
            print("Subject_name : ", Subject_name)
            print("Credits : ", Credits)
            print("Teacher : ", Teacher)
            print("=============================================================")
            if Rec_count%2 == 0:
                input("Press any key to continue: ")
                clrscreen()
                print(Rec_count, "Record(s) found")
        cnx.commit()
        Cursor.close()
        cnx.close()
    except Error as err:
        print(err)
        cnx.close()

def UpdateSubject():
    us2 = tk.Toplevel(root)
    us2.title("Update Subject")
    sidlabel = tk.Label(us2, text = 'Enter Subject_ID of Subject to be Updated :  ')
    sidlabel.grid(row=0,column=0)
    Subject_ID = tk.StringVar()#input("Enter Subject_ID of Subject to be Updated : ")
    sid = tk.Entry(us2, textvariable=Subject_ID)
    sid.grid(row=0,column=1)
    
    #print("Enter new data")
    nsidlabel = tk.Label(us2, text = 'Enter new Subject_ID:  ')
    nsidlabel.grid(row=1,column=0)
    New_Subject_ID  = tk.StringVar()#input("Enter new Subject_ID  : ")
    nsid = tk.Entry(us2, textvariable=New_Subject_ID)
    nsid.grid(row=1,column=1)
    
    snlabel = tk.Label(us2, text = 'Enter new Subject Name :  ')
    snlabel.grid(row=2,column=0)
    Subject_name = tk.StringVar()#input("Enter new Subject Name : ")
    sn = tk.Entry(us2, textvariable=Subject_name)
    sn.grid(row=2,column=1)
    
    credlabel = tk.Label(us2, text = 'Enter new Credits :  ')
    credlabel.grid(row=3,column=0)
    Credits = tk.IntVar()#int(input("Enter new Credits : "))
    cred = tk.Entry(us2, textvariable=Credits)
    cred.grid(row=3,column=1)
    
    telabel = tk.Label(us2, text = 'Enter new Teacher Name :  ')
    telabel.grid(row=4,column=0)
    Teacher = tk.StringVar()#input("Enter new Teacher Name : ")
    te = tk.Entry(us2, textvariable=Teacher)
    te.grid(row=4,column=1)
    
    button4 = tk.Button(us2,text = 'Submit', command = lambda:[UpdateSubject2(New_Subject_ID,Subject_name, Credits,Teacher, Subject_ID),us2.destroy])
    button4.grid(row=5,column=0)
    canvas14=tk.Canvas(us2)
    canvas14.pack()
    #us2.mainloop()
    
def UpdateSubject2(New_Subject_ID,Subject_name, Credits,Teacher, Subject_ID):
    try:
        cnx = sqlite3.connect(path)
        Cursor = cnx.cursor()
        
        Qry = ("UPDATE Subject SET Subject_ID=?, Subject_name=?, Credits=?, Teacher=? WHERE Subject_ID=?;")
        data = (New_Subject_ID,Subject_name, Credits,Teacher, Subject_ID)
        Cursor.execute(Qry,data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record(s) Updated Successfully.")
    except Error as err:
        print(err)
        cnx.close()
#-----------------------------------------------------------------------
#DatabaseCreate()
TablesCreate()

#def main():
root = tk.Tk()
root.geometry("300x400")
root.title("exam management system")
stud_button = tk.Button(text="Student Management", command=MenuStudent)
subman_button = tk.Button(text="Subject Management", command=MenuSubject)
exam_button = tk.Button(text="Exam Management", command=MenuExam)
exit_button = tk.Button(text="Exit", command=root.destroy)
# stud_button.grid(row=0, column=0)
# subman_button.grid(row=1, column=0)
# exam_button.grid(row=2, column=0)
# exit_button.grid(row=3, column=0)
stud_button.pack()
subman_button.pack()
exam_button.pack()
exit_button.pack()
root.mainloop()


