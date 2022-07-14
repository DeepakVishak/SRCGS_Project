import pandas as pd
import smtplib as sm
import tkinter.messagebox
from datetime import datetime
import mysql.connector as m


def core(sname,ayear,ename,eno,marks,trname,tremail,trpswd,path):

    try:
        ob=sm.SMTP("smtp.gmail.com",587)  #setting SMTP 
        ob.starttls()
        ob.login(tremail,trpswd)

        value=[]
        mydb = m.connect(
            host="localhost",
            user="root",
            password="",
            database="send_success_data"
        )
        mycursor = mydb.cursor()


        df=pd.read_csv(path)
    
    
        for(row,rowseries) in df.iterrows():
            total=rowseries.iloc[6:].sum()  #Total mark
            max_mark=marks*eno              #maximum mark(out of)
            per=(total/max_mark*100)        #percentage

#message format construction
            message='''Subject::{} {} {} {} {} {} Report Card
body:
Dear {}\n
This is from {} . I am {} Teacher of {}\n
{} {} Results,\n
{}\n
Total: {}\n
Percentage: {}'''.format(rowseries[0],rowseries[1],rowseries[2],rowseries[3],ename,ayear,\
                     rowseries[4],\
                     sname,trname,rowseries[1],\
                    ename,ayear,\
                    rowseries[6:],\
                         total,per)


        

            #sending mail 
            ob.sendmail(tremail,rowseries[5],message)
            
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

            j=[rowseries[0],rowseries[1],rowseries[2],rowseries[3],rowseries[4],rowseries[5],ename,ayear,eno,max_mark,trname,tremail,total,per,dt_string]

            content=tuple(j)
            value.append(content)
            print(value)

        sql = "INSERT INTO sender_receiver_data (roll_no,stud_name,class,division,p_name,p_mailid,exam_name,aca_year,no_sub,mark_sub,tr_name,tr_mailid,total,percent,date_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.executemany(sql, value)
        mydb.commit()
    
    #error box
    except:

        tkinter.messagebox.showerror("Failed","Failed during process!!!")
    #success box
    else:

        tkinter.messagebox.showinfo("Success","Email send sucessfully!!!")







                          
    
    
  

                
