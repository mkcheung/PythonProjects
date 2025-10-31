import os
from pathlib import Path
import pyperclip
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
def generatePassword():
    global PasswordInput
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [ choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [ choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [ choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    PasswordInput.insert(0, string=password)
    pyperclip.copy(password)


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

generatePasswordButton = Button(text="Generate Password", bg=WHITE, command=generatePassword);
generatePasswordButton.grid(row=3,column=2)

def writeToFile():
    fileAndDirectory = f"{workingDirectory}/data.txt"
    mode = "a" if os.path.exists(fileAndDirectory) else "w"
    emailUserName = EmailUsernameInput.get()
    password = PasswordInput.get()
    website = websiteInput.get()

    if not emailUserName or not password or not website:
        messagebox.showinfo(title="WARNING", message="Please don't leave any fields empty!")
    else:
        messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {emailUserName}" f"\nPassword: {password} \n Are you sure you want to save?")
        line = " | ".join([website.strip(), emailUserName.strip(), password.strip()]) + "\n"
        with open(fileAndDirectory, mode) as dataFile:
            dataFile.write(line)
        EmailUsernameInput.delete(0, END)
        websiteInput.delete(0, END)

addButton = Button(text="Add",width=36, command=writeToFile)
addButton.grid(row=4, column=1, columnspan=2)

window.mainloop()