#!/usr/bin/env python3
import csv
import sys
import random

strMandarin = "mandarin"
strPinyinWithTones = "pinyin_tones"
strPinyinWithoutTones = "pinyin_no_tones"
strTones = "tones"
strDefinition = "definition"
strLearningAid = "learning_aid"

with open(sys.argv[1], mode="r") as mandarinFile:
    csvDictReader = csv.DictReader(mandarinFile)
    vocab = list(csvDictReader)
    random.shuffle(vocab)
    numWords = len(vocab)
    print("Press enter for next word")
    for word in vocab:
      print("Pinyin: " + word[strPinyinWithoutTones] + " (" + word[strDefinition] + ")", end="")
      input("")
