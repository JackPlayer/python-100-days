from tkinter import *


def button_clicked():
    label["text"] = input.get()

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=7, pady=7)

# Label
label = Label(text="GUI Program", font=("Arial", 24, "bold"))
label.grid(row=1, column=1)

# Button
button = Button(text="Click Me", command=button_clicked)
button2 = Button(text="New Button")
button.grid(row=2, column=2)
button2.grid(row=1, column=3)

# Entry
entry = Entry(width=10)
entry.grid(row=3, column=4)

window.mainloop()
