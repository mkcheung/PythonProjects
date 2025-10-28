from pathlib import Path
import pandas

class Squrriels:
    def __init__(self):
        pass
    
    def readSquirrelData(self):
        data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv");
        furColors = data['Primary Fur Color']
        colorsToCount = {
            "colors": [],
            "counts": []
        }
        for color in ["Gray", "Cinnamon", "Black"]:
            count = furColors.value_counts().get(color)
            colorsToCount['colors'].append(color)
            colorsToCount['counts'].append(int(count))
        readout = pandas.DataFrame(colorsToCount)
        print(readout)

panda = Squrriels();
panda.readSquirrelData()