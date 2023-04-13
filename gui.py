import PySimpleGUI as sg
from main import WordChooser


def update_success_rate():
    return 0 if n_of_tentatives == 0 else (correct_guesses / n_of_tentatives) * 100


correct_guesses = 0
n_of_tentatives = 0
percent_of_success = update_success_rate()

wc = WordChooser()
sg.theme("DarkBlue12")
layout = [
    [sg.Text("Spell It!")],
    [sg.InputText(key="textInput", expand_x=True, justification="center", font="Arial 35 bold")],
    [sg.Text("Correct: 0", key="correct"), sg.Text("Nº of words tried: 0", key="attempts"), sg.Text("% of success: 0%", key="success_rate")],
    [sg.Button("Play", expand_x=True)],
    [sg.Button("Hint", expand_x=True), sg.Button("Skip", expand_x=True)],
    [sg.Button("Enter", expand_x=True)],
]

window = sg.Window(
    "SpellIt",
    layout,
    size=(550, 300),
    font="Helvetica 20",
    element_justification="center",
    return_keyboard_events=True,
)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Enter" or event == "Return:36":
        text = values["textInput"].lower()
        window["textInput"].update("")
        n_of_tentatives += 1

        if text == wc.random_word:
            correct_guesses += 1
            wc.randomize_word()
            wc.set_word()
        else:
            print("WRONG")

        percent_of_success = update_success_rate()

        window["correct"].update(f"Correct: {correct_guesses}")
        window["attempts"].update(f"Nº of words tried: {n_of_tentatives}")
        window["success_rate"].update(f"% of success: {percent_of_success:.2f}%")

    if event == "Play":
        wc.say_word()

    if event == "Skip":
        wc.randomize_word()
        wc.set_word()

window.close()
