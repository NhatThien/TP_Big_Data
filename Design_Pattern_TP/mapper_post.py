#!/usr/bin/python
import csv
import sys

reader = csv.reader(sys.stdin, delimiter="\t")
writer = csv.writer(sys.stdout, delimiter="\t", quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
	body = line[4].replace('<p>','').replace('</p>','').replace('\n',' ')

	not_empty = (len(body) != 0)

	if not_empty:
		writer.writerow([body])
