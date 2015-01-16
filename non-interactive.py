# -*- encoding: utf8 -*-
from main import *

if __name__ == "__main__":
    g = generator("words.txt")
    print("Ich fordere: Wer %s, der %s!" % (g.generateWordPair()))
