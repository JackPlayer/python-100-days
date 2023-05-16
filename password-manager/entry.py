from dataclasses import dataclass
import random
import string


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
        with open("./data.txt", "a") as file:
            file.write(f"{self.website} | {self.email_username} | {self.password.password}\n")
