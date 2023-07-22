"""ex_5_1.py"""


import argparse


try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count


def main(infile):
    """Call line_count with the infile argument."""
    line_count(infile)


if __name__ == "__main__":
    lineofText = "This program prints the number of lines in infile."
    object_ar = argparse.ArgumentParser(description=lineofText)
    object_ar.add_argument("infile", type=argparse.FileType('r'))
    args_Call = object_ar.parse_args()

    if args_Call.infile:
        line_count(args_Call.infile.name)
