#!/usr/bin/env python3
# -*- coding: utf8 -*-
import os
import gzip
import time
import re

SOURCE_DIR = os.getenv("HOME") + "/sshfs"


def process_gzip(gzfile_name, match_obj):
    gz = gzip.open(gzfile_name)
    content = list(map(lambda f: f.decode("utf-8", errors="ignore"), reversed(gz.readlines())))
    last_line = content[0].rstrip("\n")
    file_mtime = time.strftime('%b %e %X', time.localtime(gz.mtime))
    lines_time = last_line[0:15]

    fn_facility = match_obj['facility']
    fn_year = match_obj['year']
    fn_month = match_obj['month']
    fn_day = match_obj['day']

    # print("{} || {}".format(file_mtime, lines_time))
    if lines_time[0:13] != file_mtime[0:13]:
        print(f"{gzfile_name}:  {file_mtime}  {lines_time}")


def run():
    cre = re.compile("^(?P<facility>.*)-(?P<year>[0-9]{4})(?P<month>[0-9]{2})(?P<day>[0-9]{2})\\.gz")
    os.chdir(SOURCE_DIR)
    list_of_gz_files = sorted(filter(cre.search, os.listdir()), reverse=True)
    for f in list_of_gz_files:
        process_gzip(f, cre.search(f))


if __name__ == "__main__":
    run()
