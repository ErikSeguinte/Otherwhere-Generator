import PySimpleGUIQt as sg
#import PySimpleGUIWx as sg
import backend

# Very basic window.  Return values as a list

menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['Help', 'About...'], ]

verse = backend.Verse()
tone = verse.tone


layout = [
            [sg.Menu(menu_def, tearoff=False)],
            [sg.MultilineOutput(str(verse))],
            [sg.Text('Please enter your Name, Address, Phone')],
            [sg.Text('Outlook', size=(15, 1)), sg.InputText(tone['outlook'])],
            [sg.Text('Address', size=(15, 1)), sg.InputText('address')],
            [sg.Text('Phone', size=(15, 1)), sg.InputText('phone')],
            [sg.Submit(), sg.Cancel()]
            ]

window = sg.Window('Simple data entry window').Layout(layout)
button, values = window.Read()

print(button, values[0], values[1], values[2])