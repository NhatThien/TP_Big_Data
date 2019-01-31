#!/usr/bin/python

import sys
# Pour chaque ligne de la fichier d'entree
for line in sys.stdin:
	# Separer les differents champs pars tabulation
	# Retourner une liste des strings separes
	data = line.strip().split("\t")
	# Une donnee complete doit contenir 6 champs
	if len(data) ==  6:
		# Stocker linformation dune donnee
		# sous forme des differents variables
		date, time, store, item, cost, payment = data
		# Afficher store et cost
		print "{0}\t{1}".format(store, cost)
