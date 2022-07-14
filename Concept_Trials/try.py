from tkinter import *
from tkinter import ttk, StringVar
from tkinter.filedialog import askopenfilename

class GUI:

    def __init__(self,window):

        window.title("Home Page")
        window.resizable(0, 0) # this prevents from resizing the window
        window.geometry("700x300")

        #Name of School
        var1=StringVar()
        var1.set("School Name:")

        schl_name_label=Label(root,textvariable=var1,height=5).grid(row=1,column=0)
        schl_name_entry=Entry(root,bd=5).grid(row=1,column=1)

        #Name of Exam
        var2=StringVar()
        var2.set("Exam Name:")

        exam_name_label=Label(root,textvariable=var1,height=5).grid(row=2,column=0)
        exam_name_entry=Entry(root,bd=5).grid(row=2,column=1)
    
        #Academic Year
        var2=StringVar()
        var2.set("Academic Year (start-end):")

        aca_name_label=Label(root,textvariable=var1,height=5).grid(row=3,column=0)
        aca_name_entry=Entry(root,bd=5).grid(row=3,column=1)

        #No: of subjects
        var2=StringVar()
        var2.set("Number of Subjects:")

        sub_name_label=Label(root,textvariable=var1,height=5).grid(row=4,column=0)
        sub_name_entry=Entry(root,bd=5).grid(row=4,column=1)

        #Teacher name
        var2=StringVar()
        var2.set("Teacher Name :")

        sub_name_label=Label(root,textvariable=var1,height=5).grid(row=4,column=0)
        sub_name_entry=Entry(root,bd=5).grid(row=4,column=1)

        #Button
        file_upload=Button(window, text = "Users File", command = pass).grid(row = 4, column=0)

    



if __name__ == '__main__':
    
    root = Tk()
    gui = GUI(window)
    root.mainloop()
