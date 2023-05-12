import datetime
import time
from tkinter import Tk, Canvas, PhotoImage, Button, Frame
from tkinter.ttk import Label, Separator

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
NAME = "Pomodoro"

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    global timer
    reps = 0
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00", fill="white")
    status_label.config(text="")
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = SHORT_BREAK_MIN * 60

    if reps > 7:
        reset()
    if reps == 7:
        countdown(long_break_sec, color=RED, status="Long Break")
    elif reps % 2 == 0:
        countdown(work_sec, color=GREEN, status="Working")
    else:
        countdown(short_break_sec, color=PINK, status="Short Break")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count, color, status):
    global reps
    if count >= 0:
        if count == 0:
            marks = "".join("✓" for _ in range(reps) if reps % 2 == 0)
            reps += 1
            check_marks.config(text=marks)
            start()
        status_label.config(text=status, foreground=color)
        count_minutes_seconds = str(datetime.timedelta(seconds=count)).split(':')[1:]
        count_formatted = ":".join(count_minutes_seconds)
        canvas.itemconfig(timer_text, text=count_formatted, fill=color)
        global timer
        timer = window.after(1000, countdown, count - 1, color, status)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(NAME)
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(window, text="Timer", font=(FONT_NAME, 30, "bold"), background=YELLOW, foreground=GREEN)
status_label = Label(window, text="", font=(FONT_NAME, 20, "bold"), background=YELLOW, foreground=GREEN)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='./tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")

start_button = Button(text="Start", command=start, background="white", highlightthickness=0)
reset_button = Button(text="Reset", command=reset, background="white", highlightthickness=0)
check_marks = Label(text="", foreground=GREEN, font=(FONT_NAME, 20, "bold"), background=YELLOW)


title.grid(row=1, column=2)
status_label.grid(row=2, column=2)
canvas.grid(row=3, column=2)
start_button.grid(row=4, column=1)
reset_button.grid(row=4, column=3)
check_marks.grid(row=5, column=2)

window.mainloop()
