#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# Szerettem volna valami közelítő statisztikát, amiből kiderül, mely sorok ismétlődnek viszonylag
# gyakran, egy egyébként ismeretlen szerkezetű logban. Hát ez itt most kuka.
# A százalék számítás ehhez biztosan kevés és az sem jó, ahogy feldarabolom a sorokat,
# mert az így kiválogatott szavak nagy része sok esetben egy-egy szám, ami rengetegszer ismétlődik,
# de teljesen eltérő módon (egyik sorban IP cím, másikban időpont, a harmadikban csak egy random érték
# formájában és ez elviszi az átlagot úgy, mintha a sor gyakori vendég lenne a logban, holott nem az.

import sys
import re
from collections import defaultdict


def doit(input_file):
    separators_string = ' |=|;|!|->|\(|\)|\[|\]|\{|\}|\.|\+'
    print(separators_string)
    re_separators = re.compile(separators_string)    # Word separators
    words = defaultdict(lambda: 0)  # Nem kell foglalkozni azzal, hogy létező kulcs darabszámát
    #                                 akarom-e növelni, ha nem létezik a hivatkozott szó,
    #                                 automatikusan létrejön 0 kezdőértékkel.

    with open(input_file, "r", errors='ignore') as infile:
        log_array = infile.readlines()

    for next_line in log_array:
        next_line = next_line.rstrip("\n")
        words_in_the_line = re_separators.split(next_line)
        for w in words_in_the_line:
            words[w] += 1


    for next_line in log_array:
        next_line = next_line.rstrip("\n")
        words_in_the_line = re_separators.split(next_line)
        word_scores = defaultdict(lambda: 0)
        for next_word in words_in_the_line:
            word_scores[next_word] += words[next_word]/len(words)*100
        word_scores.pop('', None)
        formatstr = "{:3.4f}    " + "{}" * len(word_scores) + " --- {}"
        formatstr = "{:3.4f}  --- {}"
        avg = sum(word_scores.values())/float(len(word_scores))
#        print(formatstr.format(avg, *word_scores.items(), next_line))
        print(formatstr.format(avg, next_line))


#    for k in sorted(words, key=words.get):
#        print("{:8} {}".format(words[k], k))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = 0   # Ez már csak Python3 alatt működik. Az open file descriptor megnyitására
                        # is képes. Ha sorszámot kap név helyett, akkor az annak megfelelő file-t
                        # fogja használni. (stdin(0), stdout(1), stderr(2)

    doit(file_name)
