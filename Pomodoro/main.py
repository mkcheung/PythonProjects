from tkinter import *
from pathlib import Path
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0;
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

workingDirectory = Path(__file__).resolve().parent 
checkmark = '✓'
talliedCheckmarks = ''

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=5, bg=YELLOW)

timerLabel = Label(text='Timer', font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
timerLabel.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=f"{workingDirectory}/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

def reset():
    global talliedCheckmarks
    global reps
    window.after_cancel(timer) # cancels timer
    reps=0
    timerLabel.config(text="Timer", fg=GREEN)
    talliedCheckmarks = ''
    checkboxMarker.config(text=talliedCheckmarks)
    canvas.itemconfig(timer_text, text="00:00")


def start_timer():
    global reps
    global timer
    global talliedCheckmarks
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timerLabel.config(text="Break", fg=RED)
        count_down(long_break_secs)
    elif reps % 2:
        timerLabel.config(text="Break", fg=PINK)
        count_down(short_break_secs)
    else:
        timerLabel.config(text="Work", fg=GREEN)
        count_down(work_secs)

def count_down(count):
    global timer
    minutes = math.floor(count/60)
    seconds = count%60
    if seconds == 0:
        seconds = "00"
    minsAndSecs = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=minsAndSecs)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0:
            talliedCheckmarks += checkmark
            checkboxMarker.config(text=talliedCheckmarks)
        start_timer()


startButton = Button(text="Start", command=start_timer, highlightthickness=0, borderwidth=0, relief="flat", bg=YELLOW)
startButton.grid(row=2, column=0)

endButton = Button(text="Reset", highlightthickness=0, borderwidth=0, relief="flat", bg=YELLOW, command=reset);
endButton.grid(row=2, column=2)

checkboxMarker = Label(bg=YELLOW, fg=GREEN)
checkboxMarker.grid(row=4, column=1)

window.mainloop()