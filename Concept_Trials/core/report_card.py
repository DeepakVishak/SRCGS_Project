import pandas as pd
import smtplib as sm

ob=sm.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login('deepakvishak@gmail.com','9446750609')

df=pd.read_csv("Book1.csv")
#print(df)

for(row,rowseries) in df.iterrows():
    #print(row)
    #print(rowseries)
    total=rowseries.iloc[5:11].sum()
    #print("Total: ",total)
    per=(total/600*100)
    #print("Percentage : ",per)

    message='''Subject:: {} Class {}
body:
School name: ABC School
Dear {} of class {}
{} : {}
{} : {}
{} : {}
{} : {}
{} : {}
{} : {}
{} : {}
{} : {}
{} : {}
{} : {}
{} : {}
Total : {}
Percentage : {}'''.format(rowseries[1],rowseries[2],rowseries[1],rowseries[2],rowseries.index[0],rowseries[0],\
                          rowseries.index[1],rowseries[1],\
                          rowseries.index[2],rowseries[2],\
                          rowseries.index[3],rowseries[3],\
                          rowseries.index[4],rowseries[4],\
                          rowseries.index[5],rowseries[5],\
                          rowseries.index[6],rowseries[6],\
                          rowseries.index[7],rowseries[7],\
                          rowseries.index[8],rowseries[8],\
                          rowseries.index[9],rowseries[9],\
                          rowseries.index[10],rowseries[10],total,per)
    print(message)
    ob.sendmail('deepakvishak@gmail.com',rowseries[11],message)

print("Email send Successfully")
                          
            
