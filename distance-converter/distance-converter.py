import math
from tkinter import *


class DistanceConverter:
    def __init__(self, window: Tk):
        window.title("Distance Converter")
        window.config(pady=10, padx=10)
        self.title = Label(text="Distance Conversion")
        self.equal_to_label = Label(text="is equal to")
        self.kms_entry_variable = StringVar()
        self.miles_entry_variable = StringVar()
        self.kms_entry_variable.trace_add("write", callback=self.kms_callback)
        self.miles_entry_variable.trace_add("write", callback=self.miles_callback)
        self.miles_entry = Entry(textvariable=self.miles_entry_variable)
        self.kms_entry = Entry(textvariable=self.kms_entry_variable)
        self.miles = Label(text="Miles")
        self.kms = Label(text="Kilometers")
        self.last_entry = "kms"
        self.convert_button = Button(text="Convert", command=self.convert_callback)

        self.title.grid(row=1, column=2)
        self.miles.grid(row=2, column=1)
        self.kms.grid(row=2, column=3)
        self.miles_entry.grid(row=3, column=1)
        self.equal_to_label.grid(row=3, column=2)
        self.kms_entry.grid(row=3, column=3)
        self.convert_button.grid(row=4, column=2)

    def miles_callback(self, *args):
        self.last_entry = "miles"

    def kms_callback(self, *args):
        self.last_entry = "kms"

    def convert_callback(self, *args):
        if self.last_entry == "kms":
            self.miles_entry.delete(0, END)
            self.miles_entry.insert(0, self.kilometers_to_miles(self.kms_entry_variable.get()))
        else:
            self.kms_entry.delete(0, END)
            self.kms_entry.insert(0, self.miles_to_kilometers(self.miles_entry_variable.get()))

    @staticmethod
    def miles_to_kilometers(miles):
        return math.trunc(float(miles) * 1.60934)

    @staticmethod
    def kilometers_to_miles(kilometers):
        return math.trunc(float(kilometers) / 1.60934)


def main():
    window = Tk()
    DistanceConverter(window)
    window.mainloop()


if __name__ == "__main__":
    main()
