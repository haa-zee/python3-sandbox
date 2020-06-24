#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Ez egy próba a https://abuseipdb.com APIv2 használatára, valószínűleg kisség túlbonyolítva,
mert a pycurl modult használom, holott lehet, hogy a requests használata egyszerűbb lenne
Kell hozzá egy abuseipdb.key fájl, amiben a site-on generált saját kulcsot kell tárolni,
ez értelemszerűen ignorálva van a gitignore által, mert privát infó.

Lényegében a https://www.abuseipdb.com/api/v2/check URL-re kell hivatkozni, ha egy IP címről
akarok adatokat lekérni. Itt már a kulcsot a http headerben kell elküldeni, nem get paraméterként

Az API leírása: https://docs.abuseipdb.com/
'''
import json
import requests
import sys
import pycurl
from urllib.parse import urlencode
from io import BytesIO


def get_api_key():
	with open("abuseipdb.key","r") as keyfile:
		key = keyfile.readline().rstrip("\n")
	return key


class AbuseIPDB():
	def __init__(self, key):
		self.key = key
		self.curlObject = pycurl.Curl()


	def check(self, ipaddr):
		return None

	def get_blacklist(self):
		return None

	def check_block(self, netaddr):
		return None

	def report(self, ipaddr, *args):
		return None

	def bulk_report(self, ):
		pass

api_key = get_api_key()

if len(sys.argv)>1:
	ip_addr = sys.argv[1]
else:
	ip_addr = '127.0.0.1'


c = pycurl.Curl()
c.setopt(pycurl.HTTPHEADER, [ "Key:" + api_key, "Accept: application/json" ])

post_data = {"ipAddress":ip_addr, "verbose":"True", "maxAgeInDays":"90" }
postfields = urlencode(post_data)
storage = BytesIO()

c.setopt(pycurl.HTTPGET,1)
c.setopt(pycurl.URL, "https://www.abuseipdb.com/api/v2/check" + '?' + postfields)
c.setopt(pycurl.WRITEFUNCTION, storage.write)
c.perform()
c.close()

print(storage.getvalue())

#for i in response:
#	print(i)

