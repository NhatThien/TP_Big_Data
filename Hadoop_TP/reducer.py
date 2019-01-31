#!/usr/bin/python

import sys

'''
# "Sale" total dune "store"
salesTotal = 0
#
oldKey = None

# Lire les lignes dentree
for line in sys.stdin:
	# Separer linformation en "store" et "cost"
	data = line.strip().split("\t")
	# Verifie que une donnee doit contenir "store" et "cost"
	if len(data) != 2:
		continue
	
	# "Store" = "thisKey", "Cost" = "thisSale"
	thisKey, thisSale = data
	# Si la ligne execute ne contient pas linformation de meme "store"
	# que la ligne precedente, on affiche le nom du magasin et son "sale"
	# et on remet saleTotal a 0
	if oldKey and oldKey != thisKey:
		print "{0}\t{1}".format(oldKey, salesTotal)
		salesTotal = 0

	oldKey = thisKey
	if thisSale > salesTotal:
		salesTotal = float(thisSale)

# Affiche linformation du dernier magasin
if oldKey != None:
	print oldKey, "\t", salesTotal
'''

salesTotal = 0
nbOfSales= 0
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	
	
	thisKey, thisSale = data
	nbOfSales += 1
	salesTotal += float(thisSale)
	print "{0}\t{1}".format(nbOfSales, salesTotal)

print nbOfSales, "\t", salesTotal

