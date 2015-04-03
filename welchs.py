#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--source", help="Data in a csv file arranged in rows of duplicates with the standards first")
args = parser.parse_args()

if args.source:
	print "Hello!"
