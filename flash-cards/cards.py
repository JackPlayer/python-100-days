import json
import random


class Cards:
    def __init__(self):
        self.cards: list[dict] = self._load()
        self.current_card = self.get_random()

    def get_random(self):
        random_dict = random.choice(self.cards)
        return random_dict

    def remove(self, this: dict):
        for idx, entry in enumerate(self.cards):
            if entry == this:
                del self.cards[idx]

    def reload(self):
        self.cards = self._load()

    @staticmethod
    def _load() -> list[dict]:
        file_name = "data.json"
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError as err:
            print(f"Failed to parse {file_name}. The error was: {err}. Closing.")
            raise
        except FileNotFoundError:
            print(f"Could not find {file_name}. Closing.")
            raise
        return data
