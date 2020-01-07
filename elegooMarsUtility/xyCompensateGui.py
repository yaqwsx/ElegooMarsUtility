#!/usr/bin/env python3

import PySimpleGUI as sg
import sys
import time
from elegooMarsUtility import emUtility

layout = [
          [sg.Text("Please enter your calibration data, input and output file")],
          [sg.Text("First layer compensation:", size=(23, 1)), sg.InputText("6", size=(32, 1))],
          [sg.Text("Normal layer compensation:", size=(23, 1)), sg.InputText("0", size=(32, 1))],
          [sg.Text("Input file:", size=(10, 1)), sg.InputText(size=(30, 1)), sg.FileBrowse(size=(10, 1), file_types=(("CBDDLP Files", "*.cbddlp"),))],
          [sg.Text("Output file:", size=(10, 1)), sg.InputText(size=(30, 1)), sg.FileSaveAs(size=(10, 1), file_types=(("CBDDLP Files", "*.cbddlp"),))],
          [sg.Submit(button_text="Run", size=(25, 1)), sg.Cancel(button_text="Exit", size=(25, 1))]
         ]
window = sg.Window("Elegoo Mars utility").Layout(layout)

while True:
    button, values = window.Read()

    if button == "Exit":
        sys.exit(0)

    try:
        firstCompensation = int(values[0])
    except ValueError:
        sg.Popup("Error: first layer compensation is not a number")
        continue

    try:
        normalCompensation = int(values[1])
    except ValueError:
        sg.Popup("Error: first layer compensation is not a number")
        continue

    if len(values[2]) == 0:
        sg.Popup("Error: you have to select input file")
        continue
    inputFilename = values[2]

    if len(values[3]) == 0:
        sg.Popup("Error: you have to select output file")
        continue
    outputFilename = values[3]
    if not outputFilename.endswith(".cbddlp"):
        outputFilename += ".cbddlp"

    break
window.Close()

layout = [  [sg.Text("Applying the compensation")],
            [sg.ProgressBar(1, orientation="h", size=(20, 20), key="progress")],
         ]

window = sg.Window("Elegoo Mars utility", layout).Finalize()
progress_bar = window.FindElement("progress")
emUtility.xyCompensate(inputFilename, normalCompensation, firstCompensation, outputFilename,
    lambda x, y: progress_bar.UpdateBar(x, y))
window.Close()

sg.Popup("Done. Outputfile: {}".format(outputFilename))