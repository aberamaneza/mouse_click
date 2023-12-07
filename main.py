from pyautogui import click as pg
from tkinter import *
from tkinter import ttk
import time
from keyboard import is_pressed

root = Tk()
font = ("Helvetica", 15, "italic")
root.geometry("500x300")
root.title("auto click !")
root.resizable(height = 0, width = 0)
def buttons(x,y,text,command):
	style = ttk.Style()
	style.configure("My.TButton", padding=10, relief="flat",font=("Helvetica",10,"italic"), foreground="#ce60d6", background="#007BFF")
	button = ttk.Button(root, text=text, style="My.TButton",command=command)
	button.place(x=x,y =y)
mous = 'mous.ico'
root.iconbitmap(default=mous)
def click():
	timeclick = float(e1.get())
	clicks = int(e2.get())

	for x in range(clicks):
		if is_pressed('alt+x'):
			print("Exiting the loop.")
			break
		pg()
		time.sleep(timeclick)





l1 = Label(root,text="time clicks :",font=font).place(x=15,y=60)
e1 = Entry(root,font=font,justify="center")
e1.insert(0,0.00)
e1.place(x=130,y=60)

l2 = Label(root,text="clicks :",font=font).place(x=15,y=150)
e2 = Entry(root,font=font,justify="center")
e2.insert(0,0)
e2.place(x=130,y=150)
#root.bind("<Alt-x>", exit)
def exit():
	    root.destroy()

b1 = buttons(360,220,"start !",click)
b2 = buttons(70,220,"exit !",exit)
l1 = Label(text="stop: alt x",font=font).place(x=200,y=230)
root.mainloop()
#for x in range(10):
#	pyautogui.click()