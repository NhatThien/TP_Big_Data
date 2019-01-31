#!/usr/bin/python
import sys

word_count = {}

for line in sys.stdin:
#	print (line)
#	line.replace('<\r>','').replace('<\n>', '')
#	print (line)	
	line = line.rstrip()
	if line in word_count :
		word_count[line]+=1
	else:
		word_count[line]=1

print(word_count)
