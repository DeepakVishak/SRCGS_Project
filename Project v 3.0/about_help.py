from tkinter import *
from tkhtmlview import HTMLLabel



# Create Object
root = Tk()

root.title("About and Help")

# Set Geomerty
root.geometry("800x800")
root.resizable(0,0)

about=Label(root,text="ABOUT",fg="green",font=('Helvetica', 18, 'bold'))
credit=Label(root,text="CREDITS",fg="green",font=('Helvetica', 18, 'bold'))
# Add label
my_label = HTMLLabel(root, html="""

	<p align="center">
	<img src="icon//sw_icon.png" width="300" height="100">
	<img src="icon//icfoss-logo.png" width="300" height="100">
	</p>
	
	<table align="center" style="width:1000;height:40">
	
	<td>
	<p align="justify" style="font-size:2">
	<b>Student Report Card Generator and Sender (SRCGS)</b> System is a software aims to generate 
	report card of students including the total and percentage of each student’s academic performance
	in each examination using basic data about School name, Academic year etc.. and the mark sheet uploaded 
	as .csv file by the teachers and sends this report card using given mail id on .csv file 
	to the concerned parent or student.
	Simply it’s a 2-in-1 process report card generation and sending on a click.
	<br>
	This is the project done by Deepak V for ICFOSS Enginnering Python
	program under the guidelines of ICFOSS Team.
	</p>
	</td>
	
	</table>""")

#Add credits and instruction document link	
my_label_1 = HTMLLabel(root, html = """	
	

	<img src="icon//Credits.png" width="650" height="160">	
	

        <p align="center" style="font-size:30">Here are the instructions below:</p>
	<a href="https://drive.google.com/file/d/1q1XPOf8tiI3aXzTdgsg2KDxOzSYiV9iD/view?usp=sharing">Instructions</a>""")

 
        

# Adjust label
about.pack(pady=10, padx=10)
my_label.pack(pady=10, padx=10)

credit.pack(pady=10, padx=10)
my_label_1.pack(pady=10, padx=10)

# Execute Tkinter
root.mainloop()
