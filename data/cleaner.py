#!/usr/bin/python

with open("forum_node.tsv", "r") as _in:
	with open("clean_forum.tsv", "w") as _out:
		for l in _in.readlines():
			_out.write(l.strip()+"\n")
