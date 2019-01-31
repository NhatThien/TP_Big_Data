#!/usr/bin/python
import sys

post_count =  0
a=[]
b=[]
test = 0

for line in sys.stdin:

	if len(line) ==  0:
		continue
	else:
		a.append(line)
		test += 1

a.sort(key=lambda a: len(a[4]), reverse = True)	
for i in range(0,10):
	b.append(a[i])
b.sort(key=lambda b: len(b[4]))

print("Voila les 10 posts les plus long !")

for b1 in b:
	print(b1)
