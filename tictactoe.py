from tkinter import messagebox
from tkinter import *

root = Tk()
root.title("Tic Tac Toe")
root.geometry("300x300")
active_player=0
count=0


def onClick(button_id):
	global count
	count+=1
	global active_player
	if(active_player==0):
		active_player=1
		if(button_id==11): button11.configure(text="O",bg="white",state=DISABLED)
		elif(button_id==12): button12.configure(text="O",bg="white",state=DISABLED)
		elif(button_id==13): button13.configure(text="O",bg="white",state=DISABLED)
		elif(button_id==21): button21.configure(text="O",bg="white",state=DISABLED)
		elif(button_id==22): button22.configure(text="O",bg="white",state=DISABLED)
		elif(button_id==23): button23.configure(text="O",bg="white",state=DISABLED)
		elif(button_id==31): button31.configure(text="O",bg="white",state=DISABLED)
		elif(button_id==32): button32.configure(text="O",bg="white",state=DISABLED)
		elif(button_id==33): button33.configure(text="O",bg="white",state=DISABLED)
		gamestate()
		
		
		
	else:
		active_player=0
		if(button_id==11): button11.configure(text="X",bg="Black",state=DISABLED)
		elif(button_id==12): button12.configure(text="X",bg="Black",state=DISABLED)
		elif(button_id==13): button13.configure(text="X",bg="Black",state=DISABLED)
		elif(button_id==21): button21.configure(text="X",bg="Black",state=DISABLED)
		elif(button_id==22): button22.configure(text="X",bg="Black",state=DISABLED)
		elif(button_id==23): button23.configure(text="X",bg="Black",state=DISABLED)
		elif(button_id==31): button31.configure(text="X",bg="Black",state=DISABLED)
		elif(button_id==32): button32.configure(text="X",bg="Black",state=DISABLED)
		elif(button_id==33): button33.configure(text="X",bg="Black",state=DISABLED)
		gamestate()

def gamestate():
	#diagonal wins
	if(button11['text'] == button22['text'] == button33['text'] !=""):
		messagebox.showinfo("Information",button11['text'] + " is winner")
		root.destroy()

	elif(button13['text']== button22['text'] == button31['text']!=""):
		messagebox.showinfo("Information",button13['text'] + " is winner")
		root.destroy()

	#horizontal wins
	elif(button11['text']== button12['text'] == button13['text']!=""):
		messagebox.showinfo("Information",button11['text'] + " is winner")
		root.destroy()
		
	elif(button21['text']== button22['text'] == button23['text']!=""):
		messagebox.showinfo("Information",button21['text'] + " is winner")
		root.destroy()
		
	elif(button31['text']== button32['text'] == button33['text']!=""):
		messagebox.showinfo("Information",button31['text'] + " is winner")
		root.destroy()
	#vertical wins
	elif(button11['text']== button21['text'] == button31['text']!=""):
		messagebox.showinfo("Information",button11['text'] + " is winner")
		root.destroy()
		
	elif(button12['text']== button22['text'] == button32['text']!=""):
		messagebox.showinfo("Information",button12['text'] + " is winner")
		root.destroy()

	elif(button13['text']== button23['text'] == button33['text']!=""):
		messagebox.showinfo("Information",button13['text'] + " is winner")
		root.destroy()

	#draw
	elif(count==9):
		messagebox.showinfo("Information","Draw.")
		root.destroy()


frame=Frame(root)
frame.pack(pady=10)

button11=Button(frame,text="",height=5,width=10,command= lambda: onClick(11))
button11.grid(row=0,column=0)

button12=Button(frame,text="",height=5,width=10,command= lambda: onClick(12))
button12.grid(row=0,column=1)

button13=Button(frame,text="",height=5,width=10,command= lambda: onClick(13))
button13.grid(row=0,column=2)

button21=Button(frame,text="",height=5,width=10,command= lambda: onClick(21))
button21.grid(row=1,column=0)

button22=Button(frame,text="",height=5,width=10,command= lambda: onClick(22))
button22.grid(row=1,column=1)

button23=Button(frame,text="",height=5,width=10,command= lambda: onClick(23))
button23.grid(row=1,column=2)
text=""
button31=Button(frame,text="",height=5,width=10,command= lambda: onClick(31))
button31.grid(row=2,column=0)

button32=Button(frame,text="",height=5,width=10,command= lambda: onClick(32))
button32.grid(row=2,column=1)

button33=Button(frame,text="",height=5,width=10,command= lambda: onClick(33))
button33.grid(row=2,column=2)


root.mainloop()