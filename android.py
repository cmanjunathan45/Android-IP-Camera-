import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import numpy as np
import cv2
import webbrowser
def connect():
	if((ipEntry.get()=="")&(portEntry.get()=="" )):
		messagebox.showerror("Error","IP and Port Are Empty")
	elif(ipEntry.get()==""):
		messagebox.showerror("Error","IP Address Empty")
	elif(portEntry.get()==""):
		messagebox.showerror("Error","Port Number Empty")
	else:
		try:
			while True:
				images=requests.get("http://"+ipEntry.get()+":"+portEntry.get()+"/shot.jpg")
				video=np.array(bytearray(images.content),dtype=np.uint8)
				render=cv2.imdecode(video,-1)
				cv2.imshow("IP Cam Show",render)
				if(cv2.waitKey(1)and 0xFF==ord("q")):
					break
		except:
			messagebox.showerror("Error","IP or Port Error\n      (OR)\nNetwork Error")

def clear():
	ipEntry.delete(0,END)
	portEntry.delete(0,END)
root=tk.Tk()
root.geometry("500x400")
root.title("IP Camera | Manjunathan C")
root.iconphoto(True,tk.PhotoImage(file="icon.png"))
root.config(bg="black")
label=Label(root,text="IP Address\t       Port ",bg="#000000",fg="#ffffff",font=("courier",15,"bold italic"))
label.place(x=80,y=15)

ipEntry=Entry(root,fg="#000000",bg="#ffffff",font=("courier",15,"bold italic"),width=20,borderwidth=6)
ipEntry.place(x=80,y=50)

portEntry=Entry(root,fg="#000000",bg="#ffffff",font=("courier",15,"bold italic"),width=5,borderwidth=6)
portEntry.place(x=350,y=50)

buttonConnect=Button(root,text="Connect",fg="#000000",bg="#ffffff",font=("courier",15,"bold italic"),width=7,borderwidth=6,command=connect)
buttonConnect.place(x=200,y=100)

buttonClear=Button(root,text="Clear",fg="#000000",bg="#ffffff",font=("courier",15,"bold italic"),width=7,borderwidth=6,command=clear)
buttonClear.place(x=200,y=160)

buttonExit=Button(root,text="Exit",fg="#000000",bg="#ffffff",font=("courier",15,"bold italic"),width=7,borderwidth=6,command=root.destroy)
buttonExit.place(x=200,y=220)

buttonContact=Button(root,text="Contact",fg="#000000",bg="#ffffff",font=("courier",15,"bold italic"),width=7,borderwidth=6,command=lambda: webbrowser.open("https://github.com/cmanjunathan45/"))
buttonContact.place(x=200,y=280)
root.mainloop()
