from tkinter import *

new_text = 0

window = Tk()
window.title("Miles to Kilometer")
window.minsize(width = 200,height = 100)
window.config(padx = 20,pady = 20)

input = Entry(width = 8)
input.grid(column = 2,row = 1)

label_1 = Label(text = "Miles",font = ("Ariel",10,"normal"))
label_1.grid(column = 3,row = 1)

label_2 = Label(text = "is equal to",font = ("Ariel",10,"normal"))
label_2.grid(column = 1,row = 2)

label_3 = Label(text = "km",font = ("Ariel",10,"normal"))
label_3.grid(column = 3,row = 2)

label_4 = Label(text = new_text,font = ("Ariel",10,"normal"))
label_4.config(padx = 30)
label_4.grid(column = 2,row = 2)

def clicked():
    text = float(input.get())
    new_text = text*1.609
    label_4.config(text = new_text)

button = Button(text = "Calculate",command = clicked)
button.grid(column = 2,row = 3)

window.mainloop()