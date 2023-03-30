from random import randint


class WordChooser:
    def __init__(self) -> None:
        with open("./english_words.csv") as f:
            self.words = set(word.strip() for word in f.read().split(","))
        self.random_word = self.choose_random_word()

    def choose_random_word(self):
        return self.words[randint(0, len(self.words) - 1)]

    def randomize_word(self):
        current_word = self.random_word
        new_word = self.choose_random_word()

        if new_word != current_word:
            self.random_word = new_word
            return new_word
        else:
            return self.randomize_word()
