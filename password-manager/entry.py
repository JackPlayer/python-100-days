from dataclasses import dataclass
import random
import string
import json

@dataclass
class Password:
    password: str

    @staticmethod
    def generate_password() -> str:
        return "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(18))


@dataclass
class PasswordEntry:
    website: str
    email_username: str
    password: Password

    def save(self):
        filename = "data.json"
        new_object = {"email": self.email_username, "password": self.password.password}
        json_object = {}
        try:
            with open(filename, "r") as file:
                json_object = json.load(file)
        except FileNotFoundError:
            pass

        json_object[self.website] = new_object

        with open("./data.json", "w") as file:
            json.dump(json_object, file)

    @staticmethod
    def get_result(search: str) -> dict:
        filename = "data.json"
        entry = {}

        try:
            with open(filename, "r") as file:
                json_object: dict = json.load(file)
                entry = json_object.get(search, {})
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        return entry
