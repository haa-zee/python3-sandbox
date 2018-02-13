#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
A jelek szerint ez is működget, ezekből lassan össze lehet tákolni egy pinGUI-t :D

'''
import threading, queue, os


def prod_thread(q):
    try:
        with open(os.getenv("HOME")+"/x.x","r") as src:
            for l in src:
                line=l.rstrip("\n")
                print("IN>>> {}".format(line))
                q.put(line)
    except:
        print("Bajvan")
    q.put("*")
    return 0

def cons_thread(q):
    print("Consumer started")
    m=q.get()
    while(m!="*"):
        print("QUE--> {}".format(m))
        m=q.get()
    print("Consumer ended")
    return 0

def do_what_you_want():
    q1=queue.Queue()
    producer=threading.Thread(target=prod_thread,args=(q1,))
    consumer=threading.Thread(target=cons_thread,args=(q1,))
    consumer.start()
    producer.start()
    producer.join()
    consumer.join()


if __name__ == "__main__":
    do_what_you_want()