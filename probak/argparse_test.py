#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse


def start(args):
    print("Eredeti sys.argv:",args)
    parser = argparse.ArgumentParser(description="Teszt program")
    parser.add_argument()

if __name__ == "__main__":
    start(sys.argv)
