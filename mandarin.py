#!/usr/bin/env python3
import csv
import sys
import random

# Currently doesn't do much...
with open(sys.argv[1], mode="r") as mandarinFile:
    csvDictReader = csv.DictReader(mandarinFile)
    for i in list(csvDictReader):
        print(f"{i}")
    # print(len(list(csvDictReader)))
