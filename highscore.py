import json
import os

class HighScore:

    def __init__(self, filename = "highscores.txt"):
        self.filename = filename
        topScore = 0
        topCombo = 0
        try:
            with open(self.filename) as jsonFile:
                data = json.load(jsonFile)
                for p in data["scores"]:
                    topScore = int(p["topScore"])
                    topCombo = int(p["topCombo"])
        except:
            data = {}
            data["scores"] = []
            data["scores"].append({
            "topScore":topScore,    #sets them to 0
            "topCombo":topCombo
            })
            with open(self.filename,"w") as outFile:
                json.dump(data, outFile)

        self.topScore = topScore
        self.topCombo = topCombo


    def export(self):
        os.remove(self.filename)
        data = {}
        data["scores"] = []
        data["scores"].append({
        "topScore":self.topScore,
        "topCombo":self.topCombo
        })
        with open(self.filename,"w") as outFile:
            json.dump(data, outFile)
