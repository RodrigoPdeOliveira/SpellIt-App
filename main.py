from random import choice


class WordChooser:
    def __init__(self) -> None:
        with open("./english_words.csv") as f:
            self.csv_file = f.read().split(",")
        self.random_word = choice(self.csv_file)

    def randomize_word(self):
        current_word = self.random_word
        new_word = choice(self.csv_file)

        if new_word != current_word:
            self.random_word = new_word
            return new_word
        else:
            self.random_word = self.randomize_word()
