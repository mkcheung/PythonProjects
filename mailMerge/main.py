import os
from pathlib import Path
class MailMerge:
    def __init__(self):
        self.workingDirectory = Path(__file__).resolve().parent 
        self.inviteNames = [];
        self.letterTemplate = '';

    def getNames(self):
        with open(f"{self.workingDirectory}/Names/invited_names.txt", "r") as invitedNamesFile:
            for line in invitedNamesFile:
                self.inviteNames.append(line.strip())
    
    def getTemplate(self):
        with open(f"{self.workingDirectory}/Letters/starting_letter.txt") as startingLetterFile:
            self.letterTemplate = startingLetterFile.read()

    
    def createLetters(self):
        if len(self.inviteNames) == 0 and os.path.exists(f"{self.workingDirectory}/Letters/starting_letter.txt") == False:
            return 
        else:
            newLetter = ''
            for name in self.inviteNames:
                print(name)
                newLetter = self.letterTemplate.replace('[name]', name)
                with open(f"{self.workingDirectory}/Outputs/{name}.txt", "w") as fileWrite:
                    fileWrite.write(newLetter)


mm = MailMerge();
mm.getNames()
mm.getTemplate()
mm.createLetters()