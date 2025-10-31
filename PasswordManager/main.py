from tkinter import *
from pathlib import Path

FONT_NAME = "Courier"

WHITE = "#FFFFFF"
workingDirectory = Path(__file__).resolve().parent

window = Tk();
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
padlock_img = PhotoImage(file=f"{workingDirectory}/logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(row=0, column=1)

websiteLabel = Label(text="Website:", justify="center", anchor="center", bg=WHITE, font=(FONT_NAME,10))
websiteLabel.grid(row=1, column=0)
websiteInput = Entry(width=35)
websiteInput.grid(row=1, column=1)

EmailUsernameLabel = Label(text="Email/Username:", justify="center", anchor="center", bg=WHITE, font=(FONT_NAME,10))
EmailUsernameLabel.grid(row=2, column=0)
EmailUsernameInput = Entry(width=35, bg=WHITE)
EmailUsernameInput.grid(row=2, column=1)

Password = Label(text="Password:", justify="center", anchor="center", bg=WHITE, font=(FONT_NAME,10))
Password.grid(row=3, column=0)
PasswordInput = Entry(width=21, bg=WHITE)
PasswordInput.grid(row=3,column=1)

generatePasswordButton = Button(text="Generate Password", bg=WHITE);
generatePasswordButton.grid(row=3,column=2)
addButton = Radiobutton(text="Add", bg=WHITE)
addButton.grid(row=4, column=1)

window.mainloop()