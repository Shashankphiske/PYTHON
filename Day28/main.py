from tkinter import *

# a canvas widget is something like a canvas only it allows us to layer things
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
main_text = "00:00"
min_count_1 = int(main_text[0])
min_count_2 = int(main_text[1])
sec_count_1 = int(main_text[3])
sec_count_2 = int(main_text[4])
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    countdown(5)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    canvas.itemconfig(text_count,text = count)
    if count > 0:
        window.after(1000,countdown,count-1)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx = 100,pady = 50,bg = YELLOW)

canvas = Canvas(width = 200,height = 224,bg = YELLOW,highlightthickness = 0) # the highlightthickness eliminates the border that was being created
tomato = PhotoImage(file = "C:\\Users\\shash\\Documents\\PYTHON\\Day28\\tomato.png")
canvas.create_image(100,112,image = tomato)
text_count = canvas.create_text(101,130,text = main_text,fill = "white",font = (FONT_NAME,35,"bold"))
canvas.grid(column = 2,row = 2)

label = Label(text = "TIMER")
label.config(bg = YELLOW,fg = GREEN,font = (FONT_NAME,24,"bold"))
label.grid(column = 2,row = 1)

button_start = Button(text="START",command=start_timer)
button_start.config(bg = YELLOW,fg = RED)
button_start.grid(column = 1,row = 3)

reset_button = Button(text = "RESET")
reset_button.config(bg = YELLOW,fg = RED)
reset_button.grid(column = 3,row = 3)

check_mark = Label(text = "✔",fg = RED,bg = YELLOW)
check_mark.grid(column = 2,row = 4)
window.mainloop()