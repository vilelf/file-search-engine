import os
import pickle

from gui import Gui


class SearchEngine:
    def __init__(self):
        self.file_index = []
        self.results = []
        self.matches = 0
        self.records = 0
    
    def create_new_index(self, values):
        """create a new index and save to file"""
        root_path = values['PATH']
        self.file_index = [(root, files) for root, _, files in os.walk(root_path) if files]

        with open('file_index.pkl', 'wb') as f:
            pickle.dump(self.file_index, f)


    def load_existing_index(self):
        """load existing index"""
        try:
            with open('file_index.pkl', 'rb') as f:
                self.file_index = pickle.load(f)
        except Exception as e:
            print(e)
            self.file_index = []

    def search(self, values):
        """search for term based on search type"""
        self.results.clear()
        self.matches = 0
        self.records = 0
        term = values['TERM']

        for path, files in self.file_index:
            for file in files:
                self.records += 1
                if self._has_the_term_in_filename(term, values, file):
                    result = path.replace('\\', '/') + '/' + file
                    self.results.append(result)
                    self.matches += 1
                else:
                    continue
        with open('search_results.txt', 'w') as f:
            for row in self.results:
                f.write(row + '\n')


    def _has_the_term_in_filename(self, term, values, file):
        return (
            values['CONTAINS'] and term.lower() in file.lower() 
            or values['STARTSWITH'] and file.lower().startswith(term.lower())
            or values['ENDSWITH'] and file.lower().endswith(term.lower())
        )


def main():
    g = Gui()
    s = SearchEngine()
    s.load_existing_index()

    while True:
        event, values = g.window.read()
        if event is None:
            break
        if event == '_INDEX_':
            s.create_new_index(values)

            print()
            print('>> New Index has been created')
        if event == '_SEARCH_':
            s.search(values)

            print()
            for result in s.results:
                print(result)

            print()
            print(f'>> There were {s.matches} matches out of {s.records} records searched\n')
            print('>> This query produced the following matches: \n')
            print('>> File was saved.')
main()