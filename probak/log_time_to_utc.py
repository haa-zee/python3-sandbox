#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Logfile időpontjának konvertálása  "Hhh nn óó:pp:mm" -> timestamp
Csak 2018-as logokkal működik helyesen! (de csak arra kellett)
"""
import time
import sys
import os


def start_processing(args):
    infile = args[1]
    outfile = infile + ".secs"

    if os.path.exists(outfile):
        print("{} already exists...".format(outfile), file=sys.stderr)
        sys.exit(-1)

    try:
        with open(infile, "r") as inf, open(outfile, "w") as outf:
            for l in inf:
                tstring = l[0:15]
                mstring = l[16:]
                timestamp = time.mktime(time.strptime("2018 " + tstring, "%Y %b %d %H:%M:%S"))
                outf.write("{} {}".format(timestamp, mstring))

    except IOError as e:
        print(e)
        sys.exit(-1)


if __name__ == "__main__":
    start_processing(sys.argv)
