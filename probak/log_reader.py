#!/usr/bin/env python3
# -*- coding: utf8 -*-
import argparse
import os
import sys

class ProgramArgs:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--file", default=sys.stdin, type=argparse.FileType('r'))
        self.arguments = parser.parse_args()

class LogProcessor:
    def __init__(self, input_fd):
        self._input_fd = input_fd

    def process(self):
        for next_rec in self._input_fd:
            next_rec = next_rec.rstrip("\n")
            print("--> {}".format(next_rec))


def start_processing():
    args = ProgramArgs()
    lp = LogProcessor(args.arguments.file)
    lp.process()


if __name__ == "__main__":
    start_processing()
