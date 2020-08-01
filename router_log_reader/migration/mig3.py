#!/usr/bin/env python3
"""
Log migráció előkészítéséhez szükséges script
Feladat: megkeresni azokat a logokat, amik kizárólag olyan May  5 kezdetű sorokat tartalmaznak, amelyekben
ez az idő hamis (router reboot miatt keletkeztek)
Ezeknél a valódi időt úgy lehet megkapni (közelítőleg persze), hogy ki kell szedni
"""

import sys
import os
import glob
import re
import gzip
import time

# A helyes specifikáció valami olyan, mint a LOG_FILE_RE tartalma, de a glob.glob nem kezel regex mintákat.
LOG_FILES_SPEC = "/home/haazee/sshfs/*-*.gz"
LOG_FILES_RE = "(.*)-([0-9]{8}).gz"
MAY__5_RE = r"^May  5"


def process_file(p_filename, p_date):
	cre = re.compile(MAY__5_RE)
	"""Nem variálok, miután fix fájlokkal kell dolgozni, egyszerűbb bedrótozni, hogy minden .gz. 
	Viszont... nem nyithatom "rt" paraméterrel a fájlokat, mert akkor a kapott objektum nem tartalmazza az mtime
	változót. (undocumented: az io.TextIOWrapper objektum buffer változója a gzip.open(..., "rt",...) megnyitással
	egy gzip.GZipFile objektum lesz, amiből elvileg ki lehetne szedni az mtime értékét, de az itt használt megoldás
	legalább a dokumentált utat követi, bár sokkal rondább)
	Ezért csak "rb" módban nyitom,   így minden sor "bytes" objektumként olvasódik be. Ezt string-re 
	konvertálni a .decode metódussal lehet és kell
	"""
	with gzip.open(p_filename, "rb") as infile:
		ll = list(
			filter(lambda y: cre.search(y) is None, map(lambda x: x.decode(encoding="utf-8", errors="ignore"), infile)))
		if len(ll) == 0:
			print(p_filename, "  ", len(ll), time.strftime("%Y-%m-%d %X", time.localtime(infile.mtime)))


def start():
	log_dir = os.path.dirname(LOG_FILES_SPEC)
	log_files = os.path.basename(LOG_FILES_SPEC)

	os.chdir(log_dir)
	file_list = glob.glob(log_files)

	cre = re.compile(LOG_FILES_RE)

	# A sorted azért kell, mert tapasztalataim szerint a fájlok listáját
	# random sorrendben kapom meg, nem rendezetten
	for filename in sorted(file_list):
		s = cre.search(filename)
		if s:
			process_file(filename, s.group(1))
		else:
			print('Hibás név (pl. hiányzik a dátum):', filename, file=sys.stderr)


if __name__ == "__main__":
	start()
