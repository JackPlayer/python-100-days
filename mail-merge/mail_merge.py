output_dir = "./output"
starting_letter_path = "starting_letter.txt"
names = "names.txt"


def create_mail_letter(name: str) -> bool:
    file_name = output_dir + f"/letter_for_{name}.txt"
    try:
        with open(starting_letter_path, "r") as starting_letter:
            starting_letter_content = starting_letter.read()
            mail_letter_content = starting_letter_content.replace("[name]", name)
            with open(file_name, "w") as mail_letter:
                mail_letter.write(mail_letter_content)
            return True

    except Exception as e:
        print(e)
        return False


def create_all_mail_letters():
    try:
        with open(names, "r") as names_file:
            names_file_content = names_file.read()

            for name in names_file_content.split("\n"):
                create_mail_letter(name)
    except Exception as e:
        print(e)


def main():
    create_all_mail_letters()


if __name__ == "__main__":
    main()
