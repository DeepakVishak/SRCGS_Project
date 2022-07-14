import pandas as pd
import smtplib as sm
import tkinter.messagebox


def core(sname,ayear,ename,eno,marks,trname,tremail,trpswd,path):

    try:
        ob=sm.SMTP("smtp.gmail.com",587)
        ob.starttls()
        ob.login(tremail,trpswd)

        df=pd.read_csv(path)
    
    
        for(row,rowseries) in df.iterrows():
            total=rowseries.iloc[6:].sum()
            max_mark=marks*eno
            per=(total/max_mark*100)

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


        

        
            ob.sendmail(tremail,rowseries[5],message)
        
    
    

    except:

        tkinter.messagebox.showerror("Failed","Failed during process!!!")
  
    else:

        tkinter.messagebox.showinfo("Success","Email send sucessfully!!!")







                          
    
    
  

                
