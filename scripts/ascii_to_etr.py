#!/usr/bin/python
# p5convertfile.py
#
# 18-765: Digital Systems Testing and Testable Design
# Script used for Project 5
#
#
# Used to convert between vector file types
#
# INPUTS:
#   Starting File:
#       <inputfile>
#         ** File to convert from
#
#   Resulting File:
#        <outputfilename>
#

'''Used for conversion between vector file types'''

import sys
import optparse
import p5fileconvert
from pathlib import Path
import typer

# Checks for a couple possible errors in the data
def checkfinputs(innames, outnames, invecs, outvecs):
	'''Performs checks on data'''

	#import pdb; pdb.set_trace()

	#makes sure number of input signals matches length of input vector
	for vec in invecs:
		if not len(vec) == len(innames):
			vecnum = invecs.index(vec)
			print("Error: length of vector {} does not match defined number of inputs".format(vecnum))
			print("Vector {} : {}".format(vecnum, invecs[vecnum]))
			sys.exit(2)

	#makes sure number of ouptut signals matches length of output vector
	for vec in outvecs:
		if not len(vec) == len(outnames):
			vecnum = invecs.index(vec)
			print("Error: length of vector {} does not match defined number of outputs".format(vecnum))
			print("Vector {} : {}".format(vecnum, invecs[vecnum]))
			sys.exit(2)

	#makes sure number of input vectors and output vectors are the same
	if len(outvecs) > len(invecs):
		print('Error: more output vectors than input vectors')
		sys.exit(2)
	if len(outvecs) < len(invecs):
		print('Error: more input vectors than output vectors')
		sys.exit(2)

	#makes sure test vectors exist
	if not (invecs or outvecs):
		print('Error: no test vectors found')
		sys.exit(2)

	return


#Creates dicts for input and output signals with data gathered from input file
def makedicts(cknames, innames, outnames, invecs, outvecs):
	'''Makes dictionaries of signal data'''
	indict = {}
	for vec in invecs:
		for name in innames:
			if not name in indict:
				indict[name] = []  #dict has input signals as keys
			#vectors are stored as list of 1 'bit' strings
			indict[name].append(vec[innames.index(name)])

	outdict = {}
	for vec in outvecs:
		for name in outnames:
			if not name in outdict:
				outdict[name] = []  #dict has output signals as keys
			#vectors are stored as list of 1 'bit' strings
			outdict[name].append(vec[outnames.index(name)])


	#removes clock values from invecs, already stored in indict
	for cksig in cknames:
		ckpl = innames.index(cksig)
		for i in range(len(invecs)):
			invecs[i] = invecs[i][:ckpl] + invecs[i][ckpl+1:]

		innames.remove(cksig)

	return (indict, outdict)


# If no type is given for input file tries to find one in file
# Looks for specific strings corresponding to file types
# These strings are printed anytime file is created by script or Cadence ET
def getintype(fname):
	'''If no input file type is defined tries to detect in file'''
	infile = open(fname, 'rU')
	ftype = 'none'
	for line in infile:
		#searches for certain string within file
		if 'STIL VECTOR FILE' in line:
			ftype = 'stil'
			break
		elif 'EASY-TO-READ' in line:
			ftype = 'etr'
			break
	if ftype == 'none':
		print('Error: Input file type not recognized')
		print('Choose file of proper type or define input type option')
		sys.exit(2)

	return ftype


def main(
	infile: Path = typer.Argument(..., help="File to convert from"),
	outfile: Path = typer.Argument(..., help="File to convert to"),
) -> None:
	'''calls functions, etc'''
	# optparse used to accept arguments
	prog = "ascii_to_etr.py"
	usagedef = "usage: ./%prog "
	usageord = "infile(ascii) outfilename(etr)"
	usage = usagedef + usageord
	version = "%prog 1.0"

	parser = optparse.OptionParser(usage=usage, version=version)
	(options, args) = parser.parse_args()

	intype = 'ascii'
	outtype = 'etr'

	(cknames, innames, outnames, invecs, outvecs) = p5fileconvert.read_ascii(args[0])

	#checks for possible errors in input file data
	checkfinputs(innames, outnames, invecs, outvecs)

	#prints info from input file
	print('\n')
	print('READING FROM INPUT FILE')
	print("{} clock signals found".format(len(cknames)))
	print("{} input signals found (without clocks)".format(len(innames) - len(cknames)))
	print("{} output signals found".format(len(outnames)))
	print("{} vectors found\n".format(len(invecs)))

	#stores values in dictionaries
	(indict, outdict) = makedicts(cknames, innames, outnames, invecs, outvecs)

	p5fileconvert.write_etr(cknames, innames, indict, intype, outnames, outdict, outfile, infile)


if __name__ == '__main__':
	typer.run(main)
