#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# decorator használat, semmire se jó példával
# Sajnos azt közel sem ilyen egyszerű megoldani, hogy a decorator paramétert is kapjon
#

def decor(func):
    def modified(*args, **kwargs):
        print("Modified function - starting...")
        x = func(*args, **kwargs)
        print("Modified function - ending...")
        return x

    return modified


@decor
def myfunction(n, text=None):
    print("My function - executing... {}".format(text))
    return n + 1


if __name__ == "__main__":
    print(myfunction(10, "Na mi van?"))
    print(myfunction(1))
