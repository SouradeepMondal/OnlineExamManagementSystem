# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 15:41:45 2021

@author: Souradeep Mondal
"""
import tkinter as tk
import sqlite3
from sqlite3 import Error
from tkinter import *
from tkinter.ttk import *
path=""

def MenuSubject():
    window2=tk.Toplevel(root)
    window2.title("Subject Record Management")
    asr=tk.Button(window2,text="Add Subject Record")#, command=insertSubject)
    ssr=tk.Button(window2,text="Search Subject Record")#, command=SearchSubject)
    dsr=tk.Button(window2,text="Delete Subject Record")#, command=deleteSubject)
    usr=tk.Button(window2,text="Update Subject Record")#, command=UpdateSubject)
    re=tk.Button(window2,text="Return to Main Menu", command=window2.destroy)
    asr.grid(row=0,column=0)
    ssr.grid(row=1,column=0)
    dsr.grid(row=2,column=0)
    usr.grid(row=3,column=0)
    re.grid(row=4,column=0)
    canvas2=tk.Canvas(window2)
    canvas2.pack()
    window2.mainloop()
    
    
#def main():
root = tk.Tk()
root.geometry("300x400")
root.title("exam management system")
stud_button = tk.Button(text="Student Management")#, command=MenuStudent)
subman_button = tk.Button(text="Subject Management", command=MenuSubject)
exam_button = tk.Button(text="Exam Management")#, #command=MenuExam)
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




