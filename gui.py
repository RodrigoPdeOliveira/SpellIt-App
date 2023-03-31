import PySimpleGUI as sg
from main import WordChooser

wc = WordChooser()
sg.theme("DarkBlue12")
layout = [
    [sg.Text("Spell It!")],
    [sg.InputText(key="textInput", expand_x=True, justification="center", font="Arial 35 bold")],
    [sg.Text("Correct: "), sg.Text("Nº of words tried: "), sg.Text("% of success: ")],
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
        text = values["textInput"]
        window["textInput"].update("")

    if event == "Play":
        wc.say_word()

window.close()
