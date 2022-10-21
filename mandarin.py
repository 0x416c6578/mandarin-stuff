#!/usr/bin/env python3
import csv
import sys
import random
import argparse
import os
import glob
import time

# String constants from CSV files
strMandarin = "mandarin"
strPinyinWithTones = "pinyin_tones"
strPinyinWithoutTones = "pinyin_no_tones"
strTones = "tones"
strDefinition = "definition"
strLearningAid = "learning_aid"
strExample = "example"
strDifficulty = "difficulty"
strTimeAdded = "time_added"

vocab = None

# Argument parsing
parser = argparse.ArgumentParser(description="Learn Mandarin")
parser.add_argument(
    "fileOrFolder", type=str, help="file or directory of files to test with"
)

parser.add_argument(
    "-d",
    "--directory",
    action="store_true",
    help="use a directory of csv files -> will test using all files",
)

parser.add_argument(
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

parser.add_argument(
    "-n",
    "--newestN",
    type=int,
    help="tests the latest added n characters"
)

args = parser.parse_args()

# Load vocabulary from file(s)
path = args.fileOrFolder
files = []
if args.directory:
    if not os.path.isdir(path):
        print("Error: Must specify a path with the -d flag")
        sys.exit(0)
    files = glob.glob(path + "/*.csv")
else:
    if os.path.isdir(path):
        print("Error: Must specify a csv vocab file")
        sys.exit(0)
    files = [path]

vocab = []
for file in files:
    with open(file, mode="r") as f:
        csvDictReader = csv.DictReader(f)
        vocab += list(csvDictReader)

print("Welcome to Alex's Mandarin tester")
print("Selected options:")

# Shuffle before sorting if using newestN - this randomises words that have the same time added
random.shuffle(vocab)

# If we are testing only the newest n characters
if args.newestN is not None:
    print("- Testing newest", args.newestN, "words")
    # Sort on time added and reverse (now in newest->oldest order)
    vocab = sorted(vocab, key=lambda elem: elem[strTimeAdded])[::-1]
    # Select the newest n words
    vocab = vocab[:args.newestN]
else:
    print("- Testing all")

# Shuffle vocab list again
random.shuffle(vocab)

# Get difficulty
difficulty = 0
if args.difficulty is not None:
    print(f"- Difficulty set: {args.difficulty}")
    difficulty = int(args.difficulty)
else:
    print(f"- No difficulty set")

# Filter vocab by difficulty
vocab = list(filter(lambda word: int(word[strDifficulty]) >= difficulty, vocab))

if not args.pinyinTest:
    # Test pinyin (no tones) + translation -> character
    print("- Pinyin to character testing")
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

        print(f"  Answer: {word[strMandarin]}")
        print(f"  Difficulty: {word[strDifficulty]}")
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
print("\n\n再见")
