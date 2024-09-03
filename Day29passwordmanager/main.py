from tkinter import *
import math

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
pass_logo = PhotoImage(file="C:\\Users\\shash\\OneDrive\\Documents\\Transfer3\\PYTHON\\Day29passwordmanager\\logo.png")
canvas.create_image(100, 100, image = pass_logo)
canvas.pack()

window.mainloop()