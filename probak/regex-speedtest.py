#!/usr/bin/env python3
# -*- coding: utf8 -*-
# Kíváncsi voltam, tényleg annyira lassú-e a findall()?
# Úgy tűnik, igen. 6.71s a search, 8.8s a findall, ugyanazon az adathalmazon
import glob
import gzip
import timeit
import re


def find_regex1(log_lines):
    # cre = re.compile('^(... .. ..):..:.. \S+ \S+ DROP \S+ \S+ \S+ SRC=(\S+) DST=(\S+)')
    cre = re.compile('^(... .. ..):..:.. \S+ \S+ DROP.*SRC=(\S+) DST=(\S+)')
    n = 0
    for l in log_lines:
        s = cre.search(l)
        if s:
            n += 1
            w = (s.group(1), s.group(3))
    return (len(log_lines), n)


def find_regex2(log_lines):
    cre = re.compile('^(... .. ..):..:.. \S+ \S+ DROP.*SRC=(\S+) DST=(\S+)')
    n = 0
    for l in log_lines:
        s = cre.findall(l)
        if s and len(s[0]) > 2:
            n += 1
            w = (s[0][0], s[0][2])
    return (len(log_lines), n)


def grep_kern_gz_files(find_func):
    path = "/home/haazee/sshfs/kern-2020*.gz"
    file_list = list(glob.glob(path))

    n1 = 0
    n2 = 0

    for nextfile in file_list:
        with gzip.open(nextfile, mode='rt', encoding='utf-8', errors='ignore') as f:
            x = find_func(f.readlines())
            n1 += x[0]
            n2 += x[1]
    print(n1, "\t", n2)


print(timeit.timeit(lambda: grep_kern_gz_files(find_regex1), number=1))
print(timeit.timeit(lambda: grep_kern_gz_files(find_regex2), number=1))
