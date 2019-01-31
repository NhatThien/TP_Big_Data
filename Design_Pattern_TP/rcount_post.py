#!/usr/bin/python
import sys

post_count =  0
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 1:
		continue
	post_count += 1
	
print("Il y a ", post_count,"posts !")



