#!/usr/bin/env python3
# -*- coding: utf8 -*-
import collections
import re
import os


class Collector:

    def __init__(self):
        self._results = None

    def process(self, line):
        pass

    def get_results(self):
        return self._results


class PortScanCollector(Collector):

    def __init__(self):
        super().__init__()

    def process(self, line):
        pass


class DroppedPacketsCollector(Collector):
    """Counts DROP lines in the log, per hour, per IP address (DST=...)
    process() - extracts date + hour and the external IP from input and counts them
    get_results() - returns the collected data
    """

    def __init__(self):
        super().__init__()
        self._results = collections.Counter()
        self._compiled_re = re.compile(r'^(... .. ..):.*DROP.*DST=(\S+)')

    def process(self, line):
        found_groups = self._compiled_re.search(line)
        if found_groups:
            self._results.update([found_groups.groups()])


class UnusualLinesCollector(Collector):
    def __init__(self, pattern_list):
        super().__init__()
        self._patterns = pattern_list

    def process(self, line):
        pass


if __name__ == "__main__":
    print(os.getcwd())
    dropped_collector = DroppedPacketsCollector()
    try:
        with open("/home/haazee/sshfs/kern", "rt", encoding="utf-8", errors="ignore") as kern:
            for next_line in kern:
                dropped_collector.process(next_line)
    except EnvironmentError as e:
        print(e)
    res = dropped_collector.get_results()
    for i in res:
        print("{:>6}\t{}\t{}".format(res[i], i[0], i[1]))
