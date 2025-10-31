import os
from pathlib import Path
from tkinter import *

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

websiteLabel = Label(text="Website:", bg=WHITE)
websiteLabel.grid(row=1, column=0)
websiteInput = Entry(width=35)
websiteInput.grid(row=1, column=1, columnspan=2)
websiteInput.focus()

EmailUsernameLabel = Label(text="Email/Username:", bg=WHITE)
EmailUsernameLabel.grid(row=2, column=0)
EmailUsernameInput = Entry(width=35, bg=WHITE)
EmailUsernameInput.grid(row=2, column=1, columnspan=2)
EmailUsernameInput.insert(0, 'mars.kwong.cheung@gmail.com')

Password = Label(text="Password:", bg=WHITE)
Password.grid(row=3, column=0)
PasswordInput = Entry(width=21, bg=WHITE)
PasswordInput.grid(row=3,column=1)

generatePasswordButton = Button(text="Generate Password", bg=WHITE);
generatePasswordButton.grid(row=3,column=2)

def writeToFile():
    fileAndDirectory = f"{workingDirectory}/data.txt"
    mode = "a" if os.path.exists(fileAndDirectory) else "w"
    emailUserName = EmailUsernameInput.get()
    password = PasswordInput.get()
    website = websiteInput.get()
    line = " | ".join([website.strip(), emailUserName.strip(), password.strip()]) + "\n"
    with open(fileAndDirectory, mode) as dataFile:
        dataFile.write(line)


addButton = Button(text="Add",width=36, command=writeToFile)
addButton.grid(row=4, column=1, columnspan=2)

window.mainloop()