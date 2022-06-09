#!/usr/bin/env python3
import csv
import sys
import random
import argparse
import os
import glob

strMandarin = "mandarin"
strPinyinWithTones = "pinyin_tones"
strPinyinWithoutTones = "pinyin_no_tones"
strTones = "tones"
strDefinition = "definition"
strLearningAid = "learning_aid"
strExample = "example"

parser = argparse.ArgumentParser(description="Learn Mandarin")
parser.add_argument(
    "fileOrDir", type=str, help="file or directory of files to test with"
)
parser.add_argument(
    "-d",
    "--useDirectory",
    action="store_true",
    help="use a directory of csv files -> will test using all files",
)
args = parser.parse_args()

path = args.fileOrDir
if args.useDirectory:
    if not os.path.isdir(path):
        print("Must specify a path with the -d flag")
        sys.exit(0)
    files = glob.glob(path + "/*.csv")
else:
    if os.path.isdir(path):
        print("Must specify a csv vocab file")
        sys.exit(0)
    files = [args.fileOrDir]

vocab = []
for file in files:
    with open(file, mode="r") as f:
        csvDictReader = csv.DictReader(f)
        vocab += list(csvDictReader)

random.shuffle(vocab)

print(
    """
---------------------------------
Enter for next word
h+Enter for learning aid
q+Enter to exit
---------------------------------"""
)

for word in vocab:
    print(
        f"\nPinyin (no tones): {word[strPinyinWithoutTones]} ({word[strDefinition]})  ",
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
        example = "\n  Example: " + word[strExample]
    else:
        example = ""
    print(
        f"  Answer: {word[strMandarin]}\n  Full pinyin: {word[strPinyinWithTones]} ({word[strTones]})"
        + example
    )
