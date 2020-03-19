#import PySimpleGUIQt as sg
import PySimpleGUI as sg
import backend

# Very basic window.  Return values as a list

menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['Help', 'About...'], ]

verse = backend.Verse()
char = backend.Character()

left = sg.Column([
    [sg.Text('Verse'), sg.Stretch(), sg.Button('Randomize Verse', size= (20, 0.7)), ],
    [sg.Multiline(str(verse), key='verse')]
])
right = sg.Column([
    [sg.Text('Character'),sg.Button('Randomize Character', size=(20,0.7))],
    [sg.Multiline(str(char), key='character')]
])


layout = [
            [sg.Menu(menu_def, tearoff=False)],
            [left, right],
            [sg.Exit(size = (5, .7))]
            ]

window = sg.Window('Simple data entry window').Layout(layout)
#button, values = window.Read()
#
#print(button, values[0], values[1], values[2])

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event =='Randomize Verse':
        window['verse'].update(str(backend.Verse()))
    elif event == 'Randomize Character':
        window['character'].update(str(backend.Character()))

window.close()