from random import randint
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play


class WordChooser:
    def __init__(self) -> None:
        with open("./english_words.csv") as f:
            self.words = list(word.strip() for word in f.read().split(","))
        self.random_word = self.choose_random_word()
        self.tts_audio = self.set_word()

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

    def set_word(self):
        mp3_fp = BytesIO()
        tts = gTTS(f"{self.random_word}")
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        audio = AudioSegment.from_file(mp3_fp, format="mp3")

        return audio

    def say_word(self):
        play(self.tts_audio)
