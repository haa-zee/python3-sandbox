#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import sys
import signal
import time


def sigprocessor(signum, stack):
    print("")
    print("SIGTERM detected")
    print("p1: {}".format(signum))
    print("p2: {}".format(stack))
    sys.exit(0)


signal.signal(signal.SIGTERM, sigprocessor)
pid = os.fork()
if pid == 0:
    # Child
    ppid = os.getppid()
    print("Child sleep 3s")
    time.sleep(3)
    os.kill(ppid, signal.SIGTERM)
    os._exit(0)
else:
    # Parent
    while True:
        print(".")
        time.sleep(5)
