#!/usr/bin/env python

import argparse
import sys

parser = argparse.ArgumentParser( description="" )

parser.add_argument(
	"data_file",
	help="Path to the file we want to read.",
)

args = parser.parse_args()

print(args)
print(args.data_file)
#-------------------------------------------------------------------------------
# Are there other arguments we need?
# Answer: No, we do not need any other arguments.
#-------------------------------------------------------------------------------

args = parser.parse_args( )

#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
