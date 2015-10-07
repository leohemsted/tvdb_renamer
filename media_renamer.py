#!/usr/bin/env python3
# pylint: disable=C0103
import os
import re
import csv
import sys

if len(sys.argv) == 1:
    print("""
    media_renamer renames files according to tvdb data stored tab delimited in data.tsv. The folder
    provided must only contain media files that match the provided regex.

    Usage: python3 media_renamer.py path regex dry_run

    path: The folder containing the media
    regex: A regex that can be used to extract the episode numbers of the current naming convention
    dry_run: don't move the files, just print out renaming plan
    """)
    sys.exit(0)
directory = sys.argv[1]
regex = sys.argv[2]
dry_run = len(sys.argv) > 3

if not os.path.isdir(directory):
    raise ValueError('{} is not a valid directory'.format(directory))
else:
    print('Renaming media files in {}'.format(os.path.abspath(directory)))

with open('data.tsv', 'r', encoding='utf-8') as data:
    eps = [
        (
            int(row[0].split('x')[0]),
            int(float(row[0].split('x')[1])),
            row[1]
        )
        for row in csv.reader(data, delimiter='\t')
    ]
    for c in r'\/:*?<>|':
        for ep in eps:
            if c in ep[2]:
                raise ValueError('Illegal character {} found in {}'.format(c, ep))

print('DRY RUN: ', dry_run)
os.chdir(directory)
for fname in os.listdir():
    ext = fname.split('.')[-1]
    matches = re.search(regex, fname)
    if not matches:
        raise Exception('{} did not match r"{}"'.format(fname, regex))
    num = int(matches.group(1))
    ep = eps[num - 1]
    new = 's{:02d}e{:02d} - {}.{ext}'.format(*ep, ext=ext)

    print(fname, '->', new)
    if not dry_run:
        os.rename(fname, new)

# ###### DOUBLE EP CODE:
# num = int(re.search(regex, fname).group(1)) - 1
# num *= 2
# first_ep = eps[num]
# second_ep = eps[num + 1]
# new = 's{:02d}e{:02d}e{:02d} - {} - {}.{ext}'.format(first_ep[0],
#     first_ep[1], second_ep[1], first_ep[2], second_ep[2], ext=ext)
