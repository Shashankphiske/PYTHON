import tkinter

window = tkinter.Tk()
window.title("My First GUI")
window.minsize(width = 600,height = 300)
# used to pack our lable on the screen
input = tkinter.Entry(width = 12)
input.pack()

def clicking():
    print("I got clicked")
    text = input.get()
    my_lable = tkinter.Label(text = text, font = ("Ariel",20,"bold"))
    my_lable.pack()


button = tkinter.Button(text = "click me",command = clicking)
button.pack()



window.mainloop()