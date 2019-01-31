#!/usr/bin/python
import csv
import sys

reader = csv.reader(sys.stdin, delimiter=" ")
writer = csv.writer(sys.stdout, delimiter=" ", quoting=csv.QUOTE_ALL)

for line in reader:
	for word in line:
		writer.writerow([word])
