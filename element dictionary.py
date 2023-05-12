from tkinter import Tk, Text, Entry, Button, Label, END
import json
import os

def get_data():
    path = os.path.dirname(os.path.abspath(__file__)) + "\\data"
    with open(path, "r") as f:
        file_contents = f.read()
        data = json.loads(file_contents)
    
    return data

def search_data():
    data = get_data()

    element = (input1.get()).lower()

    try:
        output = data[element]
        output = "Symbol: " + output["symbol"] + "\nRelative atomic mass: " + output["mass"] + "\nAtomic number: " + output["atomic num"] + "\nElectron arrangement: " + output["electron"]
    except:
        output = "invalid element,\nplease enter full name of\nelement."


    output_field = Text(window,width=31,height=4)
    output_field.grid(row=4,column=0)
    output_field.insert(END,output)


# Functions

# ------------------------------------------------------------- #

# GUI

window = Tk()
window.geometry("250x180")
window.title("Elements")
window.configure(background="lightgrey")

Label(window,text="Element Dictonary",font=18,bg="lightgrey").grid(row=0,column=0)

Label(window,text="Element:",font=13,bg="lightgrey").grid(row=1,column=0)

input1 = Entry(window, width=15)
input1.grid(row=3,column=0)

output_field = Text(window,width=31,height=4)
output_field.grid(row=4,column=0)

Button(window,text="Search",command=search_data).grid(row=5,column=0)

Label(window,text="Currently contains info on elements 1-30.",bg="lightgrey").grid(row=6,column=0)


# keeps window up
window.mainloop()