#!/usr/bin/python3
# -*- encoding: utf-8 -*-


# !!!! FIGYELMEZTETÉS!  W A R N I N G      WARNING  FIIIIGYEEELEEEEEEM!!!!!
# Ez a program arra példa, hogy mit NEM szabad csinálni forkolt processzekben!
# Kíváncsi voltam, hibás működésen kívül lesz-e valami jele annak, hogy hülyeséget
# csinálok, de nem, Murphy egyik törvényének sokadik folyománya itt is él:
#
#      "A számítógép az utasításaid és nem a kívánságaid szerint működik!"
#
# Nagyon figyelni kell többek közt arra is, hogy a fork után közösek lesznek a már nyitott
# fájlok, azokból olvasni, azokba írni... hát nem feltétlenül egészséges... :)
#


import os, sys

def start():
    TESTFILE = "/tmp/testfile.txt"
    if os.path.exists(TESTFILE):
        print("Töröld a {} file-t!".format(TESTFILE), file=sys.stderr)
        sys.exit(1)

    with open(TESTFILE, "w") as outfile:
        for i in range(10000):
            msg = "{} ".format(i)*30
            outfile.write(msg+"\n")

    with open(TESTFILE, "r") as infile:
        pid = os.fork()
        if pid<0:
            print("Fork hiba", file=sys.stderr)
            sys.exit(1)

        for rec in infile:
            print("{} - {}".format(pid,rec))



    if pid>0:
        os.wait()
        os.remove(TESTFILE)

if __name__ == "__main__":
    start()
