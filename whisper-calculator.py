#! /usr/bin/env python

import argparse

def num_of_seconds(abbre):
	time_map = {
	"s" : 1,
	"m" : 1 * 60,
	"h" : 1 * 60 * 60,
	"d" : 1 * 24 * 60 * 60,
	"y" : 1 * 365 * 24 * 60 * 60 
	}
	return time_map[abbre]

def get_space(pperiod, rperiod):
	
	# One whisper data point is 12 bytes
	DATAPOINT_SIZE = 12
	return (rperiod / pperiod) * DATAPOINT_SIZE


def parse_argument(args):
	pperiod = args.precision
	rperiod = args.retention

	pperiod = int(pperiod[:-1]) * num_of_seconds(pperiod[-1])
	rperiod = int(rperiod[:-1]) * num_of_seconds(rperiod[-1])

	disk_space = get_space(pperiod, rperiod)
	print "You will need: ", disk_space, "bytes"
	

def main():
	parser = argparse.ArgumentParser(description='Whisper Calculator')

	parser.add_argument('-p', action="store", dest="precision", help='Store datapoint every Xs/m/h/d/y')
	parser.add_argument('-r', action="store", dest="retention", help='Store datapoint for Xs/m/h/d/y')


	args = parser.parse_args()
	parse_argument(args)

if __name__ == '__main__':
		main()