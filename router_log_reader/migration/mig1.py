#!/usr/bin/env python3
'''
Log migráció előkészítéséhez szükséges script
Mivel egy futásra készül, nincs különösebb szükség hibakezelésre, komolyabb paraméter ellenőrzésre,
nincs szükség arra sem, hogy minden lehetséges variációra felkészüljön (pl. azt tudom, hogy egyik
logban sincs olyan, hogy a router boot miatt a log a hibás (May 5 07) idővel kezdődik vagy végződik,
így az ilyen problémás esetekkel nem kell számolnom.
'''

import argparse
import sys
import re
import gzip
import time

MAX_DIFFERENCE = 86400


def add_year_to_log(p_line, p_date):
	year = int(p_date[0:4])
	if p_line[0:3] == "Dec" and p_date[4:6] == "01":
		year -= 1
	return "{:>04} {}".format(year, p_line)


def process_file(p_filename, p_date):
	if p_filename[-3:] == '.gz':
		opener = gzip.open
	else:
		opener = open

	print("\n{}".format(p_filename))
	with opener(p_filename, "rt", encoding='utf-8', errors='ignore') as infile:
		log_with_years = list(map(lambda l: add_year_to_log(l, p_date), infile.readlines()))
		prev_line = log_with_years[0]
		try:
			prev_time = time.mktime(time.strptime(prev_line[0:20], "%Y %b %d %X"))
		except ValueError:
			pass

		for curr_line in log_with_years:
			try:
				curr_time = time.mktime(time.strptime(curr_line[0:20], "%Y %b %d %X"))
			except ValueError:
				print("Value error\n\t{}".format(curr_line))

			diff = curr_time - prev_time
			if diff > MAX_DIFFERENCE or diff < 0:
				#				print("{:8}\n{:8}  {}\n{:8}  {}\n".format(curr_time-prev_time, curr_time, curr_line.rstrip("\n"), prev_time, prev_line.rstrip("\n")))
				print("{:8}   {}".format(diff, curr_line.rstrip("\n")))

			prev_time = curr_time
			prev_line = curr_line


def start():
	parser = argparse.ArgumentParser()
	parser.add_argument('file_list', nargs='*', default=["-"], help='log files to process')
	parsed = parser.parse_args()
	cre = re.compile(r'.*(20\d{6}).*')

	# A sorted azért kell, mert tapasztalataim szerint a fájlok listáját
	# random sorrendben kapom meg, nem rendezetten
	for filename in sorted(parsed.file_list):
		s = cre.search(filename)
		if s:
			process_file(filename, s.group(1))
		else:
			print('Hibás név (hiányzik a dátum):', filename, file=sys.stderr)


if __name__ == "__main__":
	start()
