""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
from argparse import ArgumentParser
import argparse
if __name__ == "__main__":

    ob  = ArgumentParser(description="This program applies a standard scale transform to the data in infile and writes it to outfile")
    ob.add_argument("infile", type=argparse.FileType('r'))
    ob.add_argument("outfile", type=argparse.FileType('w'))
    args_p = ob.parse_args()
    data1 = np.loadtxt(args.infile)
    mean_data = np.mean(data1)
    mndata = data1 - mean_data
    std_dvsn = np.std(mndata)
    processed = mndata / std_dvsn
    np.savetxt(args.outfile, processed,fmt='%.2e')
