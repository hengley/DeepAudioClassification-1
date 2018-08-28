# -*- coding: utf-8 -*-
import csv

import eyed3

from config import train_data_label_path

labelDic = dict()

with open(train_data_label_path, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        labelDic[row[0]] = row[1]

# Remove logs
eyed3.log.setLevel("ERROR")


def is_mono(filename):
    audiofile = eyed3.load(filename)
    return audiofile.info.mode == 'Mono'


def get_genre(filepath):
    # TODOx re-implement
    # audiofile = eyed3.load(filename)
    filename = (filepath.split("/"))[2]
    if labelDic[filename]:
        return labelDic[filename]
    else:
        return None
