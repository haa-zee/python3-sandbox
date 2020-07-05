#!/usr/bin/env python3
# -*- coding: utf8 -*-
import sys
import argparse
import io
import magic
import gzip
import log_tools


def reader(infile):
    n = 0
    for _ in infile:
        n += 1
    return n


def start():
    open_by_file_type = {'text/plain': open, 'application/gzip': gzip.open}
    file_handle = None  # csak mert a pycharm pofázik, ha nincs egyértelműen definiálva a változó
    parser = argparse.ArgumentParser()
    parser.add_argument('file_list', nargs='*', help='log file(s) text/gzip')
    parsed_args = parser.parse_args()

    dropped_counter = log_tools.DroppedPacketsCollector()

    input_files = ['-'] if len(parsed_args.file_list) == 0 else parsed_args.file_list
    for f in input_files:
        if f == '-':
            file_handle = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8', errors='ignore')
        else:
            file_type = magic.from_file(f, mime=True)
            if file_type in open_by_file_type:
                file_handle = open_by_file_type[file_type](f, mode='rt', encoding='utf-8', errors='ignore')
            else:
                print("{} Unknown file type".format(f), file=sys.stderr)
        for next_line in file_handle:
            dropped_counter.process(next_line)

    _res = dropped_counter.get_results()
    for li in _res:
        print("{:>6}\t{}\t{}".format(_res[li], li[0], li[1]))


if __name__ == "__main__":
    start()
