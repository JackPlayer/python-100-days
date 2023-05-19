from tkinter import Tk, Canvas, Label, Button, StringVar
from cards import Cards

COLOR_BLUE = "#4C4C6D"
COLOR_GREEN = "#1B9C85"
COLOR_WHITE = "#E8F6EF"
COLOR_YELLOW = "#FFE194"


class Interface:
    def __init__(self, flashcards: Cards):
        self.flashcards = flashcards
        self.window = Tk()
        self.window.title("Flashy")
        self.window.config(padx=100, pady=50, bg=COLOR_BLUE)
        self.window.geometry("1000x700")

        self.language_var = StringVar(self.window, value="French")
        self.word_var = StringVar(
            self.window, value=self.flashcards.current_card["french"]
        )
        self.usage_var = StringVar(
            self.window, value=f"Usage Rank: {self.flashcards.current_card['rank']}"
        )

        self.canvas = Canvas(
            self.window,
            width=800,
            height=500,
            bg=COLOR_GREEN,
            highlightthickness=0,
        )
        self.canvas.bind("<Button-1>", self.flashcard_clicked_callback)
        self.language = Label(
            self.canvas,
            text="French",
            bg=COLOR_GREEN,
            font=("Arial", 30, "italic"),
            fg=COLOR_WHITE,
            textvariable=self.language_var,
        )
        self.word = Label(
            self.canvas,
            text=self.flashcards.current_card["french"],
            font=("Arial", 35, "bold"),
            fg=COLOR_WHITE,
            bg=COLOR_GREEN,
            textvariable=self.word_var,
        )

        self.usage = Label(
            self.canvas,
            textvariable=self.usage_var,
            fg=COLOR_WHITE,
            bg=COLOR_GREEN,
            font=("Arial", 16, "normal"),
        )

        self.check = Button(
            self.window,
            text="✓",
            font=("Arial", 50, "bold"),
            bg=COLOR_BLUE,
            fg="green",
            highlightthickness=0,
            command=self.correct_callback,
        )
        self.cross = Button(
            self.window,
            text="✕",
            font=("Arial", 50, "bold"),
            bg=COLOR_BLUE,
            fg="red",
            highlightthickness=0,
            command=self.incorrect_callback,
        )

    def start(self):
        self.canvas.place(relx=0.5, rely=0, anchor="n")
        self.language.place(relx=0.5, rely=0.1, anchor="n")
        self.word.place(relx=0.5, rely=0.5, anchor="center")
        self.usage.place(relx=0.5, rely=0.9, anchor="s")
        self.check.place(relx=1, rely=1, anchor="s")
        self.cross.place(relx=0, rely=1, anchor="s")
        self.window.mainloop()

    def flashcard_clicked_callback(self, *args, **kwargs):

        if self.language_var.get().lower() == "french":
            self.set_flashcard_canvas(
                "English",
                self.flashcards.current_card["english"],
                self.flashcards.current_card["rank"],
                COLOR_WHITE,
                "black",
            )

        else:
            self.set_flashcard_canvas(
                "French",
                self.flashcards.current_card["french"],
                self.flashcards.current_card["rank"],
                COLOR_GREEN,
                COLOR_WHITE,
            )

    def correct_callback(self):
        self.flashcards.remove(self.flashcards.current_card)
        self.flashcards.current_card = self.flashcards.get_random()
        self.set_flashcard_canvas(
            "French",
            self.flashcards.current_card["french"],
            self.flashcards.current_card["rank"],
            COLOR_GREEN,
            COLOR_WHITE,
        )

    def incorrect_callback(self):
        self.flashcards.current_card = self.flashcards.get_random()
        self.set_flashcard_canvas(
            "French",
            self.flashcards.current_card["french"],
            self.flashcards.current_card["rank"],
            COLOR_GREEN,
            COLOR_WHITE,
        )

    def set_flashcard_canvas(
        self,
        new_language: str,
        new_word: str,
        new_rank: str,
        new_bg_color: str,
        new_font_fg_color: str,
    ):
        self.language_var.set(new_language)
        self.word_var.set(new_word)
        self.usage_var.set(f"Usage Rank: {new_rank}")
        self.canvas.configure(bg=new_bg_color)
        self.language.configure(fg=new_font_fg_color, bg=new_bg_color)
        self.word.configure(fg=new_font_fg_color, bg=new_bg_color)
        self.usage.configure(fg=new_font_fg_color, bg=new_bg_color)
