#!/usr/bin/python
import csv
import sys

reader = csv.reader(sys.stdin, delimiter="\t")
writer = csv.writer(sys.stdout, delimiter="\t", quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
	body = line[4].replace('<p>','').replace('</p>','').replace('\n',' ')

	not_empty = (len(body) != 0)
	no_ender = (body.count(".") + body.count("!") + body.count("?") == 0)
	one_ender = (body.count(".") + body.count("!") + body.count("?") == 1) and (body[-1] == "." or body[-1] == "!" or body[-1] == "?")

	if not_empty and (no_ender or one_ender) :
		writer.writerow([body])

