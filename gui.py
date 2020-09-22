import PySimpleGUI as sg


sg.ChangeLookAndFeel('Dark')

class Gui:
    def __init__(self):
        self.layout = [
            [
                sg.Text('Search Term', size=(10,1)), 
                sg.Input(size=(45,1), focus=True, key='TERM'), 
                sg.Radio('Contains', group_id='choice', key='CONTAINS', default=True), 
                sg.Radio('Starstwith', group_id='choice', key='STARTSWITH'), 
                sg.Radio('Endswith', group_id='choice', key='ENDSWITH')
            ], [
                sg.Text('Root Path', size=(10,1)), 
                sg.Input(size=(45,1), key='PATH'), 
                sg.FolderBrowse('Browse'), 
                sg.Button('Re-Index', size=(10,1), key='_INDEX_'), 
                sg.Button('Search', size=(10,1), bind_return_key=True, key='_SEARCH_')
            ],[
                sg.Output(size=(100, 30))
            ]
        ]
        self.window = sg.Window('File Search Engine').Layout(self.layout)
