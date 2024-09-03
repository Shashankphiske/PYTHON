from tkinter import *
import math

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
loop = 0  
check = "✔"
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    label.config(text = "TIMER",fg = GREEN)
    check_mark.config(text="")
    canvas.itemconfig(text_count,text = "00:00")
    global loop
    loop = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global loop
    loop += 1
    
    if loop%8 == 0:
        loop == 0
        i = LONG_BREAK_MIN
        label.config(text = "LONG BREAK",fg = RED)
    elif loop%2 == 0:
        i = SHORT_BREAK_MIN
        label.config(text = "SHORT BREAK",fg = PINK)
        check_mark.config(text = check*int((loop/2)))
    else:
        i = WORK_MIN
        label.config(text = "WORK PERIOD",fg = GREEN)
    countdown(i*60)
# ---------------------------- COUNTx`DOWN MECHANISM ------------------------------- # 
def countdown(counti):
    count_min = math.floor(counti / 60)
    count_sec = counti % 60

    if count_sec < 10:
        count_sec = "0"+str(count_sec)
    canvas.itemconfig(text_count,text = f"{count_min}:{count_sec}")
    if counti > 0:
        global timer
        timer = window.after(1000,countdown,counti-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx = 100,pady = 50,bg = YELLOW)

canvas = Canvas(width = 200,height = 224,bg = YELLOW,highlightthickness = 0) # the highlightthickness eliminates the border that was being created
tomato = PhotoImage(file = "C:\\Users\\shash\\OneDrive\\Documents\\Transfer3\\PYTHON\\Day28\\tomato.png")
canvas.create_image(100,112,image = tomato)
text_count = canvas.create_text(101,130,text = main_text,fill = "white",font = (FONT_NAME,35,"bold"))
canvas.grid(column = 2,row = 2)

label = Label(text = "TIMER")
label.config(bg = YELLOW,fg = GREEN,font = (FONT_NAME,24,"bold"))
label.grid(column = 2,row = 1)

button_start = Button(text="START",command=start_timer) 
button_start.config(bg = YELLOW,fg = RED)
button_start.grid(column = 1,row = 3)

reset_button = Button(text = "RESET",command = reset_timer)
reset_button.config(bg = YELLOW,fg = RED)
reset_button.grid(column = 3,row = 3)

check_mark = Label(fg = RED,bg = YELLOW)
check_mark.grid(column = 2,row = 4)
window.mainloop()