#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import argparse


class DirType:
    def __init__(self):
        pass

    def __call__(self, dirname):
        if not os.path.exists(dirname) or not os.path.isdir(dirname):
            raise argparse.ArgumentError(dirname)
        return dirname


def parse_arguments():
    parser = argparse.ArgumentParser()
    cmd_subparsers = parser.add_subparsers(
        title="Commands", description="Log file management commands",
        dest="CMD"
    )
    cmd_list = cmd_subparsers.add_parser("list", help="List files")
    cmd_list.add_argument("directory", type=DirType())

    cmd_view = cmd_subparsers.add_parser("view", help="View the file")
    cmd_view.add_argument("file", type=argparse.FileType('r'))

    return parser.parse_args()


if __name__ == "__main__":
    print(parse_arguments())
