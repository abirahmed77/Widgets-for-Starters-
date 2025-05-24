from tkinter import *
from datetime import date

root = Tk()
root.title("Getting Started with Widgets")
root.geometry("480x360")

label = Label(text = "Hey There!!", fg = "white", bg = "#892255", height = 1, width = 30)

name_label = Label(text = "Full Name", bg = "#838303")
name_entry = Entry()

text_box = Text(height = 3)

def display():
    name = name_entry.get()
    text_box.delete(1.0, END)
    greet = f"Hello {name}!\n"
    message = "Welcome to the Application! Today's date is : "
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, str(date.today()))
    
btn = Button(text = "Begin", command = display, height = 1, bg = "#128010", fg = "white")

label.pack()
name_label.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()