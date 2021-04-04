#!/usr/bin/env python3
# -*- coding: utf8 -*-
import requests
from html.parser import HTMLParser
import pickle   # Óvatosan használandó, nem biztonságos a doksi szerint!!!
import sys


class MyParser(HTMLParser):

    def __init__(self, *args, **kwargs):
        super(MyParser, self).__init__(convert_charrefs=True, *args, **kwargs)
        self.data_list = []
        self.in_progress = False
        self.tdclass = None

    def handle_starttag(self, tag, attrs):
        self.tdclass = None
        if tag in ("tr","td"):
            if tag == "tr":
                if len(attrs)>0:
                    self.in_progress = True
            if tag == "td":
                if attrs[0][0] == "class":
                    self.tdclass = attrs[0][1].split()

    def handle_endtag(self, tag):
        if self.in_progress and tag == "tr":
            print(*self.data_list, sep=";")
            self.in_progress = False
            self.data_list = []
        self.tdclass = None # Ez ocsmány, de a handle_data() meghívódik az endtag után is, így folyton üres mezőkkel
                            # szórta tele az outputot

    def handle_data(self, data):
        if self.in_progress and self.tdclass:
            if self.tdclass[0] == "views-field":
                self.data_list.append(data.strip())


def run(pages):
    for page in range(pages):
        resp = requests.get("https://koronavirus.gov.hu/elhunytak?page={}".format(page))
        if resp.status_code != 200:
            print("HIBA TÖRTÉNT A LETÖLTÉSKOR")     # nem feltétlenül hiba, de nekem most csak a 200 elfogadható
            sys.exit(1)
        pars = MyParser()
        pars.feed(resp.text)


if __name__ == "__main__":
    n = 1 if len(sys.argv)==1 else sys.argv[1]
    run(int(n))
