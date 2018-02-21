#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shlex, subprocess, threading, queue
E_DATA = '1'
E_COMMAND = '0'


def producer_thread(queue_object, ip_addr):
    cmd = shlex.split("/bin/ping {} -i2 -c10".format(ip_addr))

    with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as proc:
        for l in proc.stdout:
            queue_object.put(E_DATA+l.decode().rstrip("\n"))
        queue_object.put(E_COMMAND)


def consumer_thread(queue_object):
    message = queue_object.get()
    while message[0] != E_COMMAND:
        print("--> {}".format(message[1:]))
        message = queue_object.get()
    print("--- VÉGE ---")


def main():
    q = queue.Queue()
    t1 = threading.Thread(target=producer_thread, args=(q, "8.8.8.8", ))
    t2 = threading.Thread(target=consumer_thread, args=(q, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    print("Hello")
    main()
    print('Itt a vége?')
