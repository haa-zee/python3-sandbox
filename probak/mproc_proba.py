#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shlex, subprocess

print("Hello")

cmd=shlex.split("/bin/ping 172.25.1.1 -i2 -c10")
print(cmd)

with subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT) as proc:
    l=proc.stdout.readline()
    while l:
        print("-->",type(l)," ",l.decode())
        l=proc.stdout.readline()

print('Itt a vége?')

