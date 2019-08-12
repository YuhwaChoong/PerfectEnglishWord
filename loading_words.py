#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Yuhwa Choong
import os
import re
from words2value import cal_value
from tqdm import tqdm
import csv


def proc_file(file):
    # 偶数行是单词，奇数行是解释
    words = []
    with open(file, 'rb') as f:
        lines = f.read().decode("gb2312", errors="ignore")
        lines = lines.split('\n')
    for i, line in enumerate(lines):
        if i % 2 == 0:
            word = line.replace('\n', '').replace('\n\r', '').replace('\r', '').replace('\r\n', '').strip()
            words.append(word)
    return words


root_path = './Oxford'
all_words = []
all_files = []

print('walking all files')
for root, dirs, files in os.walk(root_path):
        for file in files:
            file = os.path.join(root, file)
            all_files.append(file)

print('loading all words')

for file in tqdm(all_files):
    all_words += proc_file(file)

print('all words loaded')

print('processing all words')

res = []
res2 = []
for word in tqdm(all_words):
    v, o_str = cal_value(word)
    this_res = {'word': word, 'value': v, 'o_str': o_str}
    if v == 100:
        res2.append(this_res)
    res.append(this_res)

res = [dict(t) for t in set([tuple(d.items()) for d in res])]
res2 = [dict(t) for t in set([tuple(d.items()) for d in res2])]

o_file = './output.csv'
o_path = './100.csv'

with open(o_file, 'w', encoding='utf8') as f:
    cd = csv.DictWriter(f, fieldnames=['word', 'value', 'o_str'])
    cd.writeheader()
    cd.writerows(res)


with open(o_path, 'w', encoding='utf8') as f:
    cd = csv.DictWriter(f, fieldnames=['word', 'value', 'o_str'])
    cd.writeheader()
    cd.writerows(res2)


print('done')

