import PySimpleGUI as gui
import dataclasses
from dataclasses import dataclass , asdict
import json
import requests

data = []
@dataclass
class Item:
    ID: str
    Name: str

# Loading/Downloading Item Data
def Load():
    loadlayout =[
        [ gui.Text('Choose a database to load from:') ],
        [ gui.Button('Cached Data') ],
        [ gui.Button('Data Dragon') ],
        [ gui.Button('Community Dragon') ],
        [ gui.Cancel() ]
        ]
    loadwin = gui.Window('Loading...',loadlayout)
    while True:
        loadevent,loadvalues = loadwin.read()
        if loadevent in (None, 'Cancel'):
            break
        if loadevent == 'Cached Data':
            break
        if loadevent == 'Data Dragon':
            DDragon()
            break
        if loadevent == 'Community Dragon':
            CDragon()
            break
    loadwin.close()

# Getting info from the Official Data Dragon
def DDragon():
    window.Elem('loaded').Update('Data Dragon')
    with open('item.json','r') as jfile:
        jdata = json.load(jfile)
        global data
        data = []
        for i in jdata['data'].items():
            itemid = i[0]
            item = Item(
                itemid,
                jdata['data'][itemid].get('name')
                )
            data.append(item)

# Getting info from the fanmade Community Dragon
def CDragon():
    window.Elem('loaded').Update('Community Dragon')
    global data
    data = []
    pass

# Viewing Loaded Data
def View():
    for i in data:
        for x in vars(i):
            gui.Print(asdict(i)[x])

# Editing Loaded Data
def Edit():
    pass

# Saving Current Data
def Save():
    pass

# Main Window
def main():
    gui.change_look_and_feel('DarkBlue3')
    layout = [
        [ gui.Text('Currently Stashed: ') , gui.Text('Nothing', size = (15,1), key = 'loaded') ],
        [ gui.Button('Load'),gui.Button('View') ],
        [ gui.Button('Edit'),gui.Button('Save') ],
        [ gui.Button('Quit') ]
        ]
    global window
    window = gui.Window('Dragon Stash', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Quit'):
            break
        if event == 'Load':
            Load()
        if event =='View':
            View()
    window.close()

if __name__ == "__main__":
        main()
