#!/usr/bin/env python

import argparse
import sys

parser = argparse.ArgumentParser( description="" )

parser.add_argument(
	"data_file",
	help="Path to the file we want to read.",
)

#-------------------------------------------------------------------------------
# Are there other arguments we need?
# Answer: No, we do not need any other arguments.
#-------------------------------------------------------------------------------

args = parser.parse_args( )

print("args = ", args)

print("The name of the data file is", args.data_file)

#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------

fh = open(args.data_file)

print("The file handle is", fh)

lines = 0
words = 0
chars = 0

for line in fh:
	lines += 1

print("The number of lines is", lines)

row = []

for line in fh:
	row = line.strip().split("\t")
	for i in range(len(row)):
		a = row[0]
