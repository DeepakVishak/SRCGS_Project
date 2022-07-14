from tkinter import *

root = Tk()
root.title("Home Page")
root.resizable(0, 0) # this prevents from resizing the window
root.geometry("700x500")

#Name of School
var1=StringVar()
var1.set("School Name:")

schl_name_label=Label(root,textvariable=var1,height=5).grid(row=1,column=0)
schl_name_entry=Entry(root,bd=5).grid(row=1,column=1)

#Name of Exam
var2=StringVar()
var2.set("Exam Name:")

exam_name_label=Label(root,textvariable=var2,height=5).grid(row=2,column=0)
exam_name_entry=Entry(root,bd=5).grid(row=2,column=1)
    
#Academic Year
var3=StringVar()
var3.set("Academic Year (start-end):")

aca_name_label=Label(root,textvariable=var3,height=5).grid(row=3,column=0)
aca_name_entry=Entry(root,bd=5).grid(row=3,column=1)

#Teacher name
var5=StringVar()
var5.set("Teacher Name :")

sub_name_label=Label(root,textvariable=var5,height=5).grid(row=4,column=0)
sub_name_entry=Entry(root,bd=5).grid(row=4,column=1)

#Button
file_upload=Button(root, text = "Upload Marksheet(.csv)").grid(row = 5, column=0)

root.mainloop()
