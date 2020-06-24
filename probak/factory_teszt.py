#!/usr/bin/env python3
# -*- coding: utf8 -*-


class Factory:
    @staticmethod
    def get_object(arg):
        switch = {
            1: Elso,
            2: Masodik
        }

        return switch.get(arg, lambda: "Invalid argument")()


class FactoryByString:
    @staticmethod
    def get_object(arg):
        # !!! Ez egy veszélyes játék, mert az eval _bármit_ végrehajt a futási környezet összes adatát elérve
        # Ellenőrizetlen forrásból ilyet futtatni felelőtlenség. Viszont nekem arra kell majd, hogy a program .ini file-jában
        # beállított osztály-regex párokból valódi objektum legyen a stringként beolvasott névből. Ezt teszteltem a
        # mellékelt kóddal, hogy fog-e menni?
        name = eval(arg)
        return name()


class Switchable:
    mynameis = None

    def doit(self):
        print("Type:", self.mynameis)
        return


class Elso(Switchable):
    mynameis = "Első"
    pass


class Masodik(Switchable):
    mynameis = "Második"
    pass


if __name__ == "__main__":
    f = FactoryByString().get_object("Elso")
    print(f, isinstance(f, Switchable))
    f.doit()

    f = Factory.get_object(1)
    print(f, isinstance(f, Switchable))
    f.doit()
    f = Factory.get_object(2)
    print(f, isinstance(f, Switchable))
    f.doit()
    f = Factory.get_object(3)
    print(f, isinstance(f, Switchable))
    f.doit()
