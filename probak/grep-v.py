#!/usr/bin/env python3
# -*- coding: utf8 -*-

import argparse
import re
import os
import sys


class Filter:

    def __init__(self, ffile):
        self.setup(ffile)
        self._filter_expressions = []  # Type: List[Any]
        self.regexps = []  # Type: List[Any]

    def setup(self, ffile):
        """ A "ffile" soraiból kiválogatja azokat a sorokat, amik nem #-kal kezdődnek
        (nem komment) és lecsapja a sorok végéről a NL karaktert, ezzel töltve fel
        a "filter_expressions" listát."""

        self._filter_expressions = list(
            map(lambda line: line.rstrip('\n'), filter(lambda line: line[0] != '#', ffile))
        )

        # a fenti listából "lefordított" regex lista készítése
        self.regexps = list(map(lambda re_str: re.compile(re_str), self._filter_expressions))

    def is_matching(self, string):
        """A paraméterként kapott <string> ellenőrzése, hogy a self.regexps változóban tárolt
        minták közt van-e olyan, amelyikre illeszkedik."""

        # result = list(filter(lambda a: a.search(string), self.regexps ))
        # return len(result)==0
        # A két fenti sor talán "pythonosabb", viszont iszonyat lassú és nem tudom, hogy lehetne
        # gyorsítani rajta.
        match = False
        for i in self.regexps:
            match = i.search(string)
            if match:
                break
        return match


def start():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filter", dest="file", type=argparse.FileType("r"), help="filter file",
                        default=os.devnull)
    parser.add_argument("input_file", type=argparse.FileType('r'), help="Router's kernel log file",
                        default=sys.stdin, nargs='?')
    args = parser.parse_args()

    filter_object = Filter(ffile=args.file)

    with args.input_file as kernel_log:
        for next_line in kernel_log:
            next_line = next_line.rstrip("\n")
            if not filter_object.is_matching(next_line):
                print(next_line)


if __name__ == "__main__":
    start()
