# -*- coding: utf-8 -*-
import csv

import eyed3

from config import trainDataLabel

labelDic = dict()

with open(trainDataLabel, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        labelDic[row[0]] = row[1]

# Remove logs
eyed3.log.setLevel("ERROR")


def isMono(filename):
    audiofile = eyed3.load(filename)
    return audiofile.info.mode == 'Mono'


def getGenre(filename):
    # TODOx re-implement
    # TODO have getGerne for test case
    # audiofile = eyed3.load(filename)
    if labelDic[filename]:
        return labelDic[filename]
    else:
        return None
