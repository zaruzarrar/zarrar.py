from tkinter import *
import tkinter as tk
from datetime import date 

root = tk.Tk()
root.title("getting started with widgets")
root.geometry("400x300")
lbl = Label(text="Hey there", fg="white",bg="blue",height=1, width=300)
name_lbl=Label(text="Full name",bg="aqua")
name_entry=Entry()

def display ():
    name= name_entry.get()
    global Message
    Message="Welcome to the application \n Todays date is:"
    greet="Hello"+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,Message)
    text_box.insert(END,date.today())

text_box=Text(height=3)
btn= Button(text="Begin",command=display, height=1, bg="blue",fg="white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()


    
    

