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
    raise Exception


signal.signal(signal.SIGTERM, sigprocessor)
pid = os.fork()
if pid == 0:
    # Child
    ppid = os.getppid()
    wait_time = 30
    print("Child ({}) sleep {}s".format(os.getpid(), wait_time))
    time.sleep(wait_time)
    os.kill(ppid, signal.SIGTERM)
    os._exit(0)
else:
    # Parent
    try:
        while True:
            print("Parent pid: {}".format(os.getpid()))
            time.sleep(5)
    except:
        pass
    finally:
        print("O.K., befejeztem")
sys.exit(1)
