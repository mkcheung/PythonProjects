import os
from pathlib import Path
import pandas

class NATOAlphabet:
    def __init__(self):
        self.natoDictionary = ''
        self.nameToTranslate = []
        self.name = ''

    def getName(self):
        self.name = input("Input name to translate into phonetics: ")

    def createNATOList(self):
        workingDirectory = Path(__file__).resolve().parent 
        data = pandas.read_csv(f"{workingDirectory}/nato_phonetic_alphabet.csv")

        self.natoDictionary = { row['letter']:row['code'] for (index, row) in data.iterrows()}

    def nameToPhonetics(self):
        for char in self.name:
            self.nameToTranslate.append([ value for (key, value) in self.natoDictionary.items() if key == char.capitalize()])
        

natoAlphabet = NATOAlphabet()
natoAlphabet.createNATOList()
natoAlphabet.getName()
natoAlphabet.nameToPhonetics()
print(natoAlphabet.nameToTranslate)