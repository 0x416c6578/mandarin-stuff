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
strExample = "example"

with open(sys.argv[1], mode="r") as mandarinFile:
    csvDictReader = csv.DictReader(mandarinFile)
    vocab = list(csvDictReader)
    random.shuffle(vocab)
    numWords = len(vocab)
    print(
        """
---------------------------------
enter for next word
\"h\" enter for learning aid
\"q\" enter to exit
---------------------------------"""
    )
    for word in vocab:
        print(
            f"\nPinyin (no tones): {word[strPinyinWithoutTones]} ({word[strDefinition]})  ",
            end="",
        )
        bruh = input("")
        if "q" in bruh:
            print("再见！")
            sys.exit(0)
        if "h" in bruh:
            if len(word[strLearningAid]) > 0:
                print(f"  {word[strLearningAid]}  ", end="")
            else:
                print(f"  No learning aid available  ", end="")
            input("")
        print(f"  Answer: {word[strMandarin]}, example: {word[strExample]}")
