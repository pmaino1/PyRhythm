import json
import os

class HighScore:

    def __init__(self, filename = "highscores.txt"):
        """
        Creates a file containing the top score and the top combo.
        param:(object,file) needs self and a filename
        return (None)
        """
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
        """
        Deletes the existing file and creates a new one with updated information.
        param:(object) only needs self
        return: (None)
        """
        os.remove(self.filename)
        data = {}
        data["scores"] = []
        data["scores"].append({
        "topScore":self.topScore,
        "topCombo":self.topCombo
        })
        with open(self.filename,"w") as outFile:
            json.dump(data, outFile)
