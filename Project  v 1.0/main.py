from tkinter import *
from tkinter import ttk, StringVar
from tkinter.filedialog import askopenfilename
import tkinter.messagebox
from core import core


class Home_Page_GUI:

    def __init__(self,window):

        window.title("Home Page")
        window.resizable(0,0)
        window.geometry("800x700")

        self.input_schl_name = StringVar()
        self.input_aca_year = StringVar()
        self.input_exam_name = StringVar()
        self.input_exam_no = IntVar()
        self.input_marks = IntVar()
        self.input_tchr_name = StringVar()
        self.input_tchr_email = StringVar()
        self.input_tchr_paswd = StringVar()
        self.input_path = StringVar()
        
        self.sname = ''
        self.ayear = ''
        self.ename = ''
        self.eno = 0
        self.marks = 0
        self.trname = ''
        self.tremail = ''
        self.trpswd = ''
        self.path = ''

        self.input_exam_no.set('')
        self.input_marks.set('')

        #Title of application
        title=Label(window,bg='white',text='Student Report Card Generator and Sender',fg='red',font='50',padx='20',pady='20')
        title.grid(row=0,column=1)

        
        #School Name
        Schl_name_label=Label(window,text='School Name : ',height=3).grid(row=1,column=0)
        Schl_name_entry=Entry(window,textvariable=self.input_schl_name ,bd=5).grid(row=1,column=1,ipadx=30)

        #Academic Year
        Aca_name_label=Label(window,text='Academic Year : ',height=3).grid(row=2,column=0)
        Aca_name_entry=Entry(window,textvariable=self.input_aca_year ,bd=5).grid(row=2,column=1,ipadx=30)

        #Exam Name  
        Exam_name_label=Label(window,text='Exam Name : ',height=3).grid(row=3,column=0)
        Exam_name_entry=Entry(window,textvariable=self.input_exam_name ,bd=5).grid(row=3,column=1,ipadx=30)

        #No: of exams
        Exam_no_label=Label(window,text='No: of Exams : ',height=3).grid(row=4,column=0)
        Exam_no_name_entry=Entry(window,textvariable=self.input_exam_no  ,bd=5).grid(row=4,column=1,ipadx=30)

        #Marks per subject
        Marks_label=Label(window,text='Marks per subject : ',height=3).grid(row=5,column=0)
        Marks_entry=Entry(window,textvariable=self.input_marks  ,bd=5).grid(row=5,column=1,ipadx=30)

        #Teacher Name
        Tr_name_label=Label(window,text='Teacher Name: ',height=3).grid(row=6,column=0)
        Tr_name_entry=Entry(window,textvariable=self.input_tchr_name,bd=5).grid(row=6,column=1,ipadx=30)

        #Teacher Email
        Tr_Email_label=Label(window,text='Teacher Email ID (*Only Gmail) : ',height=3).grid(row=7,column=0)
        Tr_Email_entry=Entry(window,textvariable=self.input_tchr_email ,bd=5).grid(row=7,column=1,ipadx=30)

        #Teacher Email Password
        Tr_Email_pswd_label=Label(window,text='Teacher Email ID Password: ',height=3).grid(row=8,column=0)
        Tr_Email_pswd_entry=Entry(window,textvariable=self.input_tchr_paswd ,bd=5,show='*').grid(row=8,column=1,ipadx=30)

        #upload Marksheet
        upload_marksheet_button=Button(window, text = "Upload Marksheet in (*.csv format)", command = lambda: self.set_path_users_field()).grid(row=9,column=0,ipadx=5,ipady=15) 
        upload_marksheet_label=Label(window, textvariable = self.input_path, width = 70).grid( row = 9, column = 1, ipadx=1, ipady=1)

        #Final Submit
        submit=Button(window, text = "SUBMIT" ,fg='green',font='20',command= lambda: self.action()).grid(row=10,column=1,ipadx=20,ipady=10)

        
        Rights=Label(window,text='© All rights reserved.DeepakV ICFOSS Project',height=13).grid(row=11,column=1)

    def set_path_users_field(self):
        self.path = askopenfilename() 
        self.input_path.set(self.path)

    def assign(self):

        self.sname = self.input_schl_name.get()
        self.ayear = self.input_aca_year.get()
        self.ename = self.input_exam_name.get()
        self.eno = self.input_exam_no.get()
        self.marks= self.input_marks.get()
        self.trname = self.input_tchr_name.get()
        self.tremail = self.input_tchr_email.get()
        self.trpswd = self.input_tchr_paswd.get()
        self.path = self.input_path.get()

    def action(self):
        submit=tkinter.messagebox.askquestion("Submit","Are you sure to you want to proceed with this action?")

        if submit=='yes':


            self.assign()
            core(self.sname,self.ayear,self.ename,self.eno,self.marks,self.trname,self.tremail,self.trpswd,self.path)


                    


if __name__ == '__main__':
    window = Tk()
    gui = Home_Page_GUI(window)
    window.mainloop()
        
