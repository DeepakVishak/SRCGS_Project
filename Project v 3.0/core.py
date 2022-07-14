import pandas as pd
import smtplib as sm
import tkinter.messagebox


def core(sname,ayear,ename,eno,marks,trname,tremail,trpswd,path):

    try:
        ob=sm.SMTP("smtp.gmail.com",587)  #setting SMTP 
        ob.starttls()
        ob.login(tremail,trpswd)

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
        
    
    
    #error box
    except:

        tkinter.messagebox.showerror("Failed","Failed during process!!!")
    #success box
    else:

        tkinter.messagebox.showinfo("Success","Email send sucessfully!!!")







                          
    
    
  

                
