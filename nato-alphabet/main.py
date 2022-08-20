import pandas


class NATOAlphabet:
    def __init__(self):
        self.alphabet: pandas.DataFrame = self._load_alphabet_csv(file_name="nato_phonetic_alphabet.csv")
        self.conversion_dict = {row.letter: row.code for (index, row) in self.alphabet.iterrows()}
        self.conversion_dict[' '] = ' '

    def get_nato_list_from_word(self, word: str) -> list[str]:
        return [self.conversion_dict[char] for char in word]

    @staticmethod
    def _load_alphabet_csv(file_name: str) -> pandas.DataFrame:
        return pandas.read_csv(file_name)

    @staticmethod
    def ask_for_word():
        word = input("Insert a word: ")
        return word.upper()


def main():
    print("--- NATO ALPHABET CONVERTER ---")
    alphabet = NATOAlphabet()
    word = alphabet.ask_for_word()
    print(alphabet.get_nato_list_from_word(word))


if __name__ == "__main__":
    main()
