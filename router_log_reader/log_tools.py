#!/usr/bin/env python3
# -*- coding: utf8 -*-
import collections
import re
import os
import sys

MINIMUM_HIT_COUNT = 5  # If TCP+UDP port count greater than this, then it is a port scan.

DROPPED_PACKETS_RE = r'^(... .. ..):.*DROP.*DST=(\S+)'
PORT_SCAN_RE = r"(... ..) (..:..:..) (\S+) (\S+): DROP.*SRC=(\S+) DST=(\S+) .*PROTO=(TCP|UDP) .*SPT=(\S+) .*DPT=(\S+)"


class Collector:

    def __init__(self):
        self._results = None

    def process(self, line):
        pass

    def get_results(self):
        return self._results


class DroppedPacketsCollector(Collector):
    """Counts DROP lines in the log, per hour, per IP address (DST=...)
    process() - extracts date + hour and the external IP from input and counts them
    get_results() - returns the collected data
    """

    def __init__(self):
        super().__init__()
        self._results = collections.Counter()
        self._compiled_re = re.compile(DROPPED_PACKETS_RE)

    def process(self, line):
        found_groups = self._compiled_re.search(line)
        if found_groups:
            self._results.update([found_groups.groups()])


class UnusualLinesCollector(Collector):
    def __init__(self, pattern_list):
        super().__init__()
        self._results = []
        self._patterns = [li.rstrip("\n")
                          for li in filter(lambda lin: len(lin) > 0 and not lin.isspace(), pattern_list)]
        self.compiled_regex = re.compile("(" + ")|(".join(self._patterns) + ")")

    def process(self, line):
        if not self.compiled_regex.search(line):
            self._results.append(line)


class PortScanCollector(Collector):

    def __init__(self):
        super().__init__()
        self._results = collections.defaultdict(
            lambda: {'TCP': collections.defaultdict(lambda: 0), 'UDP': collections.defaultdict(lambda: 0)}
        )
        self.compiled_regex = re.compile(PORT_SCAN_RE)

    def process(self, line):
        s = self.compiled_regex.search(line)
        if s:
            group_list = s.groups()
            self._results[group_list[4]][group_list[6]][group_list[8]] += 1

    def get_results(self):
        x = sorted(self._results, key=lambda s: len(self._results[s]['TCP']) + len(self._results[s]['UDP']))
        w = []
        for i in x:
            tcp_count = len(self._results[i]['TCP'])
            udp_count = len(self._results[i]['UDP'])
            if tcp_count + udp_count > MINIMUM_HIT_COUNT:
                w.append([i, tcp_count, udp_count])
        return w


if __name__ == "__main__":
    print("Ez csak tesztre kellett - futtasd a log_read.py-t!")
    _ = os.getcwd()
    sys.exit(-1)

'''
    print(os.getcwd())
    pattern_file = open(os.path.join(os.path.dirname(sys.argv[0]), "kern-pattern2.txt"))
    pattern_list = pattern_file.readlines()
    unusual_collector = UnusualLinesCollector(pattern_list)
    dropped_collector = DroppedPacketsCollector()
    port_scan_collector = PortScanCollector()

    try:
        with open("/home/haazee/sshfs/kern-20200705", "rt", encoding="utf-8", errors="ignore") as kern:
            for next_line in kern:
                w = next_line.rstrip("\n")
                dropped_collector.process(w)
                unusual_collector.process(w)
                port_scan_collector.process(w)
    except EnvironmentError as e:
        print(e)

    res = unusual_collector.get_results()
    for i in res:
        print(i)
    res = dropped_collector.get_results()
    for i in res:
        print("{:>6}\t{}\t{}".format(res[i], i[0], i[1]))
    res = port_scan_collector.get_results()
    for i in res:
        print("{:15}\t{:>8}\t{:>8}\t{:>8}".format(i[0],i[1],i[2],i[1]+i[2]))
'''
