from tkinter import *
from math import floor
from winsound import Beep
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_str = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def raise_window(window):
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
def reset_timer():i
    global reps
    start["state"] = "active"
    window.after_cancel(timer)
    reps = 0
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text = "")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    start["state"] = "disabled"
    if reps % 2 == 1:
        minutes = WORK_MIN
        timer_label.config(text = "Work", fg = GREEN)
    elif reps % 8 == 0:
        minutes = LONG_BREAK_MIN
        timer_label.config(text="Long Break", fg= RED)
    else:
        minutes = SHORT_BREAK_MIN
        timer_label.config(text="Short Break", fg= PINK)

    countdown(minutes * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps
    global check_str
    #mm = floor(count/60)
    #mm = count // 60
    #ss = count % 60
    mm, ss = divmod(count, 60)

    # Both ways can be used
    # canvas.itemconfig(timer_text, text = f"{mm}:{(str(ss)).zfill(2)}")
    canvas.itemconfig(timer_text, text=f"{mm:01}:{ss:02}")
    if count > 0:
        global timer
        # 1 sec = 1000 ms
        timer = window.after(1000, countdown, count - 1)
    else:
        #raise_window(window)
        Beep(500, 500)
        if (reps % 2 - 1) == 0:
            check_str += "✓"
            check.config(text = check_str)
        start_timer()
        # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.attributes("-topmost", 1)
window.attributes("-topmost", 0)
window.title("Podomoro")
window.config(width = 500, height = 500, padx = 100, pady = 50, bg = YELLOW)
def say_sth(a,b):
    print(a)
    print(b)
# 1 sec = 1000 ms


# Canvas enable image and object overlapping
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = ("Courier New", 30, "bold"))
canvas.grid(row = 1, column = 1)
#canvas.pack()
#countdown(5)

timer_label = Label(text = "Timer", fg = GREEN, font = ("Arial", 24, "bold"), bg = YELLOW)
timer_label.grid(row = 0, column = 1)

start = Button(text = "Start", command = start_timer)
start.grid(row=2, column=0)

reset = Button(text = "Reset", command = reset_timer)
reset.grid(row = 2, column = 2)

check = Label(bg = YELLOW)
check.grid(row = 3, column = 1)





window.mainloop()