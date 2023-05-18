from tkinter import Tk, PhotoImage, Canvas, Label, Entry, StringVar, Button, END, messagebox, W, E
from entry import PasswordEntry, Password


class Manager:
    def __init__(self):
        self.window = Tk()

        self.website_entry_var = StringVar(self.window)
        self.email_entry_var = StringVar(self.window)
        self.password_entry_var = StringVar(self.window)

        self.entry = PasswordEntry("", "", password=Password(""))
        self.window.title("Password Manager")
        self.window.config(padx=100, pady=50, bg="white")

        self.canvas = Canvas(width=200, height=189, bg="white", highlightthickness=0)
        self.logo = PhotoImage(file='./logo.png')
        self.canvas.create_image(100, 100, image=self.logo)
        self.website_label = Label(self.window, text="Website", background="white")
        self.website_entry = Entry(self.window, textvariable=self.website_entry_var)
        self.search_button = Button(text="Search", command=self.search_callback,
                                               background="white")

        self.email_label = Label(self.window, text="Email/Username", background="white")
        self.email_entry = Entry(self.window, textvariable=self.email_entry_var)

        self.password_label = Label(self.window, text="Password", background="white")
        self.password_entry = Entry(self.window, textvariable=self.password_entry_var)

        self.generate_password_button = Button(text="Generate Password", command=self.generate_password_callback,
                                               background="white")

        self.add_password_button = Button(text="Add", command=self.add_password_callback, background="white")

        self.canvas.grid(row=0, column=2)
        self.website_label.grid(row=1, column=1, pady=10)
        self.website_entry.grid(row=1, column=2, pady=10)
        self.search_button.grid(row=1, column=3, pady=10,  sticky=W + E)

        self.email_label.grid(row=2, column=1, pady=10)
        self.email_entry.grid(row=2, column=2, padx=10, pady=10, columnspan=2, sticky=W + E)
        self.password_label.grid(row=3, column=1, pady=10)
        self.password_entry.grid(row=3, column=2, pady=10)
        self.generate_password_button.grid(row=3, column=3, pady=10)
        self.add_password_button.grid(row=4, column=2, columnspan=2, sticky=W + E)
        self.window.mainloop()

    def generate_password_callback(self):
        password: str = Password.generate_password()
        self.window.clipboard_clear()
        self.window.clipboard_append(string=password)
        self.password_entry.delete(first=0, last=END)
        self.password_entry.insert(index=0, string=password)

    def add_password_callback(self):
        entry = PasswordEntry(
            email_username=self.email_entry_var.get(),
            password=Password(password=self.password_entry_var.get()),
            website=self.website_entry_var.get()

        )

        if entry.password.password and entry.email_username and entry.website:
            entry.save()
        else:
            messagebox.showwarning(title="Warning", message="Please make sure all the fields are filled")

    def search_callback(self):
        search_result = PasswordEntry.get_result(search=self.website_entry_var.get())

        if search_result:
            try:
                message = f"{self.website_entry_var.get()}:\nEmail: {search_result['email']}\nPassword: {search_result['password']}"
            except KeyError:
                message = f"Could not retrieve the email or password for {self.website_entry_var.get()}"
        else:
            message = f"No results were found for {self.website_entry_var.get()}"
        messagebox.showinfo("Results", message)

if __name__ == "__main__":
    manager = Manager()
