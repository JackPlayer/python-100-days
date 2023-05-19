from cards import Cards
from interface import Interface

if __name__ == "__main__":
    flashcards = Cards()
    interface = Interface(flashcards=flashcards)

    interface.start()
