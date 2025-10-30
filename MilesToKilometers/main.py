import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(300, 200)

milesLabel = tkinter.Label(text="Miles", font=("Arial", 12, "bold"))
milesLabel.grid(row=0, column=2)
input = tkinter.Entry(width=25)
input.grid(row=0, column=1)
miles = 0;

term = tkinter.Label(text="is equal to", font=("Arial", 12, "bold"))
term.grid(row=1, column=0)

kilometers = tkinter.Label(text="0", justify="center", anchor="center", font=("Arial", 12, "bold"))
kilometers.grid(row=1, column=1)

kilometersLabel = tkinter.Label(text="Km", font=("Arial", 12, "bold"))
kilometersLabel.grid(row=1, column=2)

def calculateMiToKm():
    miles = input.get()
    kilometers.config(text=(float(miles) * 1.609344)) 

button = tkinter.Button(text="Calculate", command=calculateMiToKm)
button.grid(row=2, column=2)

window.mainloop()