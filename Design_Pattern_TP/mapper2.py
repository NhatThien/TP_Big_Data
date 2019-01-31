#!/usr/bin/python

import csv
import sys

def mapper2 ():
	a = []
	b = []
	reader = csv.reader(sys.stdin, delimiter="\t")
	writer = csv.writer(sys.stdout, delimiter = "\t", quotechar = '"', quoting = csv.QUOTE_ALL)

	for line in reader:
		#line[4].replace('<p>','').replace('</p>','').replace('\n',' ')

		if len(line[4]) ==  0:
			continue
		else:
			a.append(line)
	
	a.sort(key=lambda a: len(a[4]), reverse = True)

	for i in range(0,10):
		b.append(a[i])
	b.sort(key=lambda b: len(b[4]))
	
	for b1 in b:
		writer.writerow([b1])

mapper2()

