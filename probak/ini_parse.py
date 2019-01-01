#!/usr/bin/env python3
# -*- coding: utf8 -*-

import configparser
import argparse
import sys
import os

'''
A program feladata: configparser modul demója, próbája, tesztje.
Kaphat paramétert futtatáskor: -c|--config amivel meg lehet adni a konfig fájl nevét,
amennyiben az eltér a "programfájl neve.ini"-től.
(default név az ini_file_name = os.path... kezdetű sorban, a .splitext leválasztja a kiterjesztést
a teljes névből)
Az add_argument metódus type paraméterében megadott FileType hatására a parser megnyitja a 
fájlt ('r' = read only)
A ConfigParser osztály read_file() metódusa ezt a nyitott fájlt kapja paraméterként és beolvassa
belőle a paramétereket.
A ConfigParser.sections() adja vissza a "[valami név]" formában megadott szakaszok neveit,
a .items(...) a paraméterben megadott szakasz elemeit/értékeit. Egyesével a get...() metódusokkal
lehet lekérni ugyanezeket.

'''


def teszt():
    arg_parser = argparse.ArgumentParser()
    ini_file_name = os.path.splitext(sys.argv[0])[0] + ".ini"
    arg_parser.add_argument('-c', '--config', default=ini_file_name, dest='config',
                            type=argparse.FileType('r'),
                            help='Config file (.ini)', nargs=1)
    parsed_args = arg_parser.parse_args()
    print(parsed_args)

    conf_parser = configparser.ConfigParser()
    conf_parser.read_file(parsed_args.config)

    for i in conf_parser.sections():
        print("{} : {}".format(i, conf_parser.items(i)))

    print(conf_parser.getboolean('router', 'debug'))


if __name__ == "__main__":
    teszt()
