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

    ob = ArgumentParser(description="This program applies a standard scale transform to the data in infile and writes it to outfile.")
    
    ob.add_argument("infile", type=argparse.FileType('r'))
    
    ob.add_argument("outfile", type=argparse.FileType('w'))
    
    infileData = np.loadtxt(INFILE)
    mn = np.mean(infileData)
    mn_0 = infileData - mn
    std_mean = np.std(mn_0)
    processed = mn_0 / std_mean
    np.savetxt(OUTFILE, processed,fmt='%.2e')
