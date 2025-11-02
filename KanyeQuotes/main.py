from pathlib import Path
from tkinter import *
import requests
workingDirectory = Path(__file__).resolve().parent 
backgroundImagePath = f"{workingDirectory}/background.png"

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=f"{backgroundImagePath}")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)


def get_quote():
    global quote_text
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote_text, text=data['quote'])


kanyeImagePath = f"{workingDirectory}/kanye.png"
kanye_img = PhotoImage(file=f"{kanyeImagePath}")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()