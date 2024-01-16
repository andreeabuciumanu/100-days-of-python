from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 30
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    # timer text - 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title_label - Timer
    timer_label.config(text="Timer")
    # reset check marks
    check_label.config(text="")
    # reset the reps back to 0
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = LONG_BREAK_MIN * 60
    working_list = [1, 3, 5, 7]
    short_break_list = [2, 4, 6]
    if reps < 9:
        if reps in working_list:
            count_down(work_time)
            timer_label.config(text="WORK", fg=GREEN)
        elif reps in short_break_list:
            count_down(short_break_sec)
            timer_label.config(text="Break", fg=PINK)
        else:
            count_down(long_break_sec)
            timer_label.config(text="Break", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_minutes = math.floor(count/60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)  # count-1 is the argument for count_down()
    else:
        marks = ""
        working_sessions = math.floor(reps/2)
        for _ in range(working_sessions):
            marks += "✓"
        check_label.config(text=marks)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="TIMER", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_label = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
