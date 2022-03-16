#!/usr/bin/env python3
import csv
import sys
import random

# Currently doesn't do much...
with open(sys.argv[1], mode="r") as mandarinFile:
    csvDictReader = csv.DictReader(mandarinFile)
    # print(random.choice(list(csvDictReader)))
    print(len(list(csvDictReader)))
