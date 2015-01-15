# -*- encoding: utf8 -*-
__author__ = 'Simon, André'

import random
import json


class generator(object):
    def __init__(self, filename):
        self.verbs = dict(action=list(), consequence=list())
        self.filename = filename
        self.verbs = json.loads(open(self.filename).read())
        self.newWords = 0
        pass

    def saveList(self):
        with open(self.filename, "w") as f:
            f.write(json.dumps(self.verbs))
        pass

    def addWord(self, category, word):
        cat = ""
        if category == 1:
            cat = "action"
        elif category == 2:
            cat = "consequence"
        if word not in self.verbs[cat]:
            self.verbs[cat].append(word)
            self.newWords += 1
            if self.newWords >= 2:
                self.newWords = 0
                self.saveList()
                print("\nSaved\n--------\n\n")
        pass

    def generateWordPair(self):
        r1 = random.randint(0, len(self.verbs["action"])-1)
        r2 = random.randint(0, len(self.verbs["consequence"])-1)
        return self.verbs["action"][r1], self.verbs["consequence"][r2]

if __name__ == "__main__":
    g = generator("words.txt")
    count = 0
    while True:
        print("Ich fordere: Wer %s, der %s!" % (g.generateWordPair()))
        g.addWord(1, input("action: "))
        g.addWord(2, input("consequence: "))
        count += 1
        if count > 20:
            quit()