#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os
import json
master=Tk()
master.geometry('400x400')
mytext=StringVar()
mytex=IntVar()
mytex=0

tabcontrol=Notebook(master)
tab1=Frame(tabcontrol)
tab2=Frame(tabcontrol)
tab3=Frame(tabcontrol)
tab4=Frame(tabcontrol)
tab5=Frame(tabcontrol)
tab6=Frame(tabcontrol)
tabcontrol.add(tab1,text='New Student')
tabcontrol.add(tab2,text='Display')
tabcontrol.add(tab3,text='Course Creation')
tabcontrol.add(tab4,text='Display Courses')
tabcontrol.add(tab5,text='couse Allocation')
tabcontrol.add(tab6,text='Show couse Allocation')
tabcontrol.pack(fill=BOTH)
def message():
    messagebox.showinfo('save','your record')

def clear():
        e.delete(0,'end')
        e2.delete(0,'end')
        e3.delete(0,'end')
        e4.delete(0,'end')
def check():
    global mytex
    if(mytex==0):
        mytex=1
    else:
        mytex=0


def save():
    rollnos=[]
    if os.path.isfile('student.json'):
        with open('student.json','r')as f:
            stu=json.load(f)
        stu_list=stu['students']
        for i in stu_list:
            rollnos.append(i['Roll_no.']) 
    
    stu1={}
    stu={}
    name=e.get()
    rollno=e2.get()
    if(rollno not in rollnos):
        gender=mytext.get()
        adress=e3.get()
        phone_no=e4.get()
        batch='Batch'+combo.get()
        Hostel=True if mytex==1 else False

        stu1['Roll_no.']=rollno
        stu1["Name"]=name
        stu1['gender']=gender
        stu1['Address']=adress
        stu1['Phone_no']=phone_no
        stu1['Batch']=batch
        stu1['Hostel']=Hostel
        stu['students']=list()
        if os.path.isfile('student.json'):
            with open('student.json','r')as f:
                stu=json.load(f)
                stu['students'].append(stu1)
            
            with open('student.json','w')as f:
                json.dump(stu,f)
        else:
             with open('student.json','w')as f:
                stu['students'].append(stu1)
                json.dump(stu,f)

   
        messagebox.showinfo('save','your record has been saved')
    else:
         messagebox.showinfo('Error','your  has this record')
   
    treeview.insert('','end',values=( stu['students'][-1]['Roll_no.'],  stu['students'][-1]['Name'],  stu['students'][-1]['gender'],  stu['students'][-1]['Address'],  stu['students'][-1]['Phone_no'],  stu['students'][-1]['Batch'],  stu['students'][-1]['Hostel']))
    

        
   




Label(tab1,text='Enter Your Name').grid(row=0,column=0)
e=Entry(tab1,width='80')
e.grid(row=0,column=3,columnspan=2,pady='10')
Label(tab1,text='Enter Your Rollno').grid(row=1,column=0)
e2=Entry(tab1,width='80')
e2.grid(row=1,column=3,columnspan=2,pady='10')
Label(tab1,text='Choose your Gender').grid(row=2,column=0)
b1=Radiobutton(tab1,text='Male',variable=mytext,value='Male')
b1.grid(row=3,column=3,padx='1')
b2=Radiobutton(tab1,text='Female',variable=mytext,value='Female')
b2.grid(row=3,column=4,padx='1')
Label(tab1,text='Address for Cosepondence').grid(row=4,column=0)
e3=Entry(tab1,width='80')
e3.grid(row=4,column=3,columnspan=2 ,pady='10')
Label(tab1,text='Phone No').grid(row=5,column=0)
e4=Entry(tab1,width='80')
e4.grid(row=5,column=3,columnspan=2 ,pady='10')
Label(tab1,text='Your Batch').grid(row=6,column=0)

data=('2018','2019','2020')
combo=Combobox(tab1,value=data)
combo.grid(row=6,column=4)
Label(tab1,text='Hostel[Y/N]').grid(row=7,column=0)
c1=Checkbutton(tab1,text='Check if you want Hostel facility',variable=mytex,command=check)
c1.grid(row=7,column=4)
b3=Button(tab1,text='Save',width=20,command=lambda:save())
b3.grid(row=8,column=1)
b3=Button(tab1,text='Clear',width=20,command=lambda:clear())
b3.grid(row=8,column=2)

col=('Rollno','Name','Gender','Address','PhoneNo','Batch',"Hostel")
treeview=Treeview(tab2,height=14,show='headings',columns=col)
treeview.column('Rollno',width=140,anchor=CENTER)
treeview.column('Name',width=60,anchor=CENTER)
treeview.column('Gender',width=100,anchor=CENTER)
treeview.column('Address',width=100,anchor=CENTER)
treeview.column('PhoneNo',width=100,anchor=CENTER)
treeview.column('Batch',width=100,anchor=CENTER)
treeview.column('Hostel',width=100,anchor=CENTER)

treeview.heading(0,text='Rollno')
treeview.heading(1,text='Name')
treeview.heading(2,text='Gender')
treeview.heading(3,text='Address')
treeview.heading(4,text='PhoneNo')
treeview.heading(5,text='Batch')
treeview.heading(6,text='Hostel')
treeview.pack(side=TOP,fill=BOTH)
if os.path.isfile('student.json'):
    with open('student.json','r') as f:
        stu=json.load(f)
    for i in stu['students']:
        treeview.insert('','end',values=(i['Roll_no.'],i['Name'],i['gender'],i['Address'],i['Phone_no'],i['Batch'],i['Hostel']))
    










dat=[]

def show():
    global dat
    courseid=e5.get()
    cName=e6.get()
    c1={}
    c2={}
    c2['CourseId']=courseid
    c2['CourseName']=cName
    c1['courses']=list()
    if os.path.isfile('course.json'):
        with open('course.json','r') as f:
            c1=json.load(f)
            
            c1['courses'].append(c2)
           
        with open('course.json','w')as f:
            json.dump(c1,f)
            
           
    else:
         with open('course.json','w')as f:
            c1['courses'].append(c2)
            json.dump(c1,f)
           
           
    messagebox.showinfo('save','your record')
    
    tree.insert('','end',values=( c1['courses'][-1]['CourseId'], c1['courses'][-1]['CourseName']))
    dat.append(c1['courses'][-1]['CourseName'])
    c['values']=dat
    

def remove():
    e5.delete(0,'end')
    e6.delete(0,'end')
            
Label(tab3,text='Course ID').grid(row=0,column=0,padx=100)
e5=Entry(tab3,width=60)
e5.grid(row=0,column=2,pady=10)
Label(tab3,text='Course Name').grid(row=1,column=0)
e6=Entry(tab3,width=60)
e6.grid(row=1,column=2,pady=10)
b4=Button(tab3,text='Save',width=10,command=show)
b4.grid(row=2,column=1,pady=10)
b5=Button(tab3,text='Clear',width=10,command=remove)
b5.grid(row=2,column=2,pady=10)

col=("CourseID",'CourseName')
tree=Treeview(tab4,show='headings',columns=col,height=7)
tree.column('CourseID',width=80,anchor=CENTER)
tree.column('CourseName',width=80,anchor=CENTER)

tree.heading(0,text='CourseID')
tree.heading(1,text='CourseName')
tree.pack(fill=BOTH,side=TOP)


if os.path.isfile('course.json'):
    with open('course.json') as f:
        c1=json.load(f)
    for i in c1['courses']:
        tree.insert('','end',values=(i['CourseId'],i['CourseName']))
        dat.append(i['CourseName'])
        


def details():
    show={}
    fast={}
    roll=e7.get()
    s=c.get()
    fast['Roll']=roll
    fast['Course']=s
    show['pls']=list()
    if os.path.isfile('alloaction.json'):
        with open('alloaction.json') as f:
            show=json.load(f)
            show['pls'].append(fast)
            
        with open('alloaction.json','w') as f:
            json.dump(show,f)
    else:
         with open('alloaction.json','w') as f:
            show['pls'].append(fast)
            json.dump(show,f)
    messagebox.showinfo('save','your alloaction')
    
    t.insert('','end',values=( show['pls'][-1]['Roll'], show['pls'][-1]['Course']))
            
        
    

Label(tab5,text='Student Rollno').grid(row=0,column=0,sticky='ew',padx=200,pady=20)
e7=Entry(tab5,width=80)
e7.grid(row=0,column=2,pady=10)

Label(tab5,text='Course Name').grid(row=1,column=0)

c=Combobox(tab5,value=dat,width=80)
c.grid(row=1,column=2)
bb=Button(tab5,width=10,text='Allocate',command=details)
bb.grid(row=2,column=1,sticky='ew',pady=20)

col=('Rollno','Course')

t=Treeview(tab6,height=5,columns=col,show='headings')
t.column('Rollno',width=70,anchor=CENTER)
t.column('Course',width=80,anchor=CENTER)
t.heading('Rollno',text='Rollno')
t.heading('Course',text='Course')
t.pack(fill=BOTH,side=TOP)
if os.path.isfile('alloaction.json'):
    with open('alloaction.json','r') as f:
        show=json.load(f)
    for i in show['pls']:
        t.insert('','end',values=(i['Roll'],i['Course']))


master.mainloop()


# In[ ]:





# In[ ]:




