from tkinter import *
from tkhtmlview import HTMLLabel



# Create Object
root = Tk()

# Set Geomerty
root.geometry("600x600")

# Add label
my_label = HTMLLabel(root, html="""

	<h1 align="center"><font color="Green" size="20">ABOUT</font></h1><br>

	<p align="center">
	<img src="E:\ICFOSS\Project\icon\icon_2.png" width="300" height="100">
	<img src="E:\ICFOSS\Project\icon\icfoss-logo.png" width="300" height="100">
	</p>
	
	<table align="center" style="width:1000;height:40">
	<tr>
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
	</tr>
	</table>""")
	
my_label_1 = HTMLLabel(root, html = """	<h1 align="center"><font color="Green" size="20">CREDITS</font></h1><br>
	<table align="center"  cellspacing="15" style="font-size:30" >

	
	<tr>
	<td align="center">Dr. Elizabeth Sherly</td>
	<td align="center">DIRECTOR OF ICFOSS</td>
	</tr>
	
	<tr>
	<td align="center">Dr. Rajeev RR</td>
	<td align="center">PROGRAM HEAD</td>
	</tr>
	
	<tr>
	<td align="center">Ms.SEEMA U</td>
	<td align="center">PROJECT MENTOR</td>
	</tr>
	
	
	<tr>
	<td align="center">Mr.Navaneeth K</td>
	<td align="center">INSTRUCTOR 1</td>
	</tr>

	<tr>
	<td align="center">Ms.SANDHINI S</td>
	<td align="center">INSTRUCTOR 2</td>
	</tr>
    
	<tr>
	<td colspan="2"><font align="center">All other ICFOSS Technical and Non Technical Team</td>
	</tr>
	</table>

        <br>
        <p align="center" style="font-size:30">Here are the instructions below:</p>
	<a href="www.google.com">Instructions</a>""")

 
        

# Adjust label
my_label.pack(pady=10, padx=10)
my_label_1.pack(pady=10, padx=10)


# Execute Tkinter
root.mainloop()
