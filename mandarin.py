#!/usr/bin/env python3
import csv
import sys
import random
import argparse
import os
import glob
import time

# String constants
strMandarin = "mandarin"
strPinyinWithTones = "pinyin_tones"
strPinyinWithoutTones = "pinyin_no_tones"
strTones = "tones"
strDefinition = "definition"
strLearningAid = "learning_aid"
strExample = "example"
strDifficulty = "difficulty"

vocab = None

# Argument parsing
parser = argparse.ArgumentParser(description="Learn Mandarin")
parser.add_argument(
    "fileOrFolder", type=str, help="file or directory of files to test with"
)

parser.add_argument(
    "-f",
    "--useFolder",
    action="store_true",
    help="use a directory of csv files -> will test using all files",
)

parser.add_argument(
    "-d",
    "--difficulty",
    type=int,
    help="min difficuly (from 1 to 5) to test from - to skip easy words",
)

parser.add_argument(
    "-c",
    "--characterTest",
    action="store_true",
    help="tests pinyin (no tones) + translation -> character",
)

parser.add_argument(
    "-p",
    "--pinyinTest",
    action="store_true",
    help="tests character -> pinyin + tones + translation",
)
args = parser.parse_args()

# Load vocabulary from file(s)
path = args.fileOrFolder
files = []
if args.useFolder:
    if not os.path.isdir(path):
        print("Must specify a path with the -d flag")
        sys.exit(0)
    files = glob.glob(path + "/*.csv")
else:
    if os.path.isdir(path):
        print("Must specify a csv vocab file")
        sys.exit(0)
    files = [path]

vocab = []
for file in files:
    with open(file, mode="r") as f:
        csvDictReader = csv.DictReader(f)
        vocab += list(csvDictReader)

# Shuffle vocab list
random.shuffle(vocab)

difficulty = 0
if args.difficulty != None:
    print(f"Difficulty set: {args.difficulty}")
    difficulty = int(args.difficulty)
else:
    print(f"No difficulty set")

vocab = list(filter(lambda word: int(word[strDifficulty]) >= difficulty, vocab))

print("Mandarin learning aid program")

if not args.pinyinTest:
    # Test pinyin (no tones) + translation -> character
    print("Pinyin to character testing (default)")
    numWords = len(vocab)
    i = 1
    for word in vocab:
        print(
            f"\n---------------- {i}/{numWords} ----------------\n"
            f"Pinyin (no tones): {word[strPinyinWithoutTones]} ({word[strDefinition]})  ",
            end="",
        )
        inp = input("")
        if "q" in inp:
            print("再见！")
            sys.exit(0)
        if "h" in inp:
            if len(word[strLearningAid]) > 0:
                print(f"  {word[strLearningAid]}  ", end="")
            else:
                print(f"  No learning aid available  ", end="")
            input("")
        if word[strExample] != "":
            example = "  Example: " + word[strExample] + "\n"
        else:
            example = "\n"

        print(f"  Answer: {word[strMandarin]} (difficulty {word[strDifficulty]})")
        time.sleep(0.12)
        print(f"  Full pinyin: {word[strPinyinWithTones]} ({word[strTones]})")
        time.sleep(0.12)
        print(example, end="")
        time.sleep(0.12)
        i += 1

elif not args.characterTest and args.pinyinTest:
    # Test character -> pinyin + tones + translation
    print("Character to pinyin testing (from -p flag)")
    numWords = len(vocab)
    i = 1
    for word in vocab:
        print(
            f"\n---------------- {i}/{numWords} ----------------\n"
            f"Character: {word[strMandarin]}   ",
            end="",
        )
        inp = input("")
        if "q" in inp:
            print("再见！")
            sys.exit(0)

        print(f"  Answer: {word[strPinyinWithTones]} ({word[strTones]})")
        time.sleep(0.12)
        print(f"  Translation: {word[strDefinition]}")
        time.sleep(0.12)
        i += 1
print("再见！")