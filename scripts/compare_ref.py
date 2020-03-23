import os
import sys
import argparse
import edlib
'''

    James M. Ferguson (j.ferguson@garvan.org.au)
    Genomic Technologies
    Garvan Institute
    Copyright 2020

    script description

    For comparing 2 sequences, getting basic scores, and a "nice" alignmnet print
    out. Good for testing reference genomes with small differences between them


    ----------------------------------------------------------------------------
    version 0.0 - initial



    TODO:
        -

    ----------------------------------------------------------------------------
    MIT License

    Copyright (c) 2020 James Ferguson

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
'''

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

def print_verbose(message, level):
    '''verbose printing'''
    if VERBOSE >= level:
        sys.stderr.write('info: %s\n' % message)


def print_err(message):
    '''error printing'''
    sys.stderr.write('error: %s\n' % message)


def main():
    '''
    do the thing
    '''
    NAME = "Sequence comparison"
    VERSION = "0.1.0"


    parser = MyParser(
        description="Compare two sequences")
    # group = parser.add_mutually_exclusive_group()
    parser.add_argument("-r1", "--ref1",
                        help="input fastq file")
    parser.add_argument("-r2", "--ref2",
                        help="reference file for mapping")
    parser.add_argument("-v", "--verbose", type=int, default=1,
                        help="Engage higher output verbosity")
    parser.add_argument("-V", "--version", action="store_true",
                        help="Engage higher output verbosity")

    args = parser.parse_args()

    # print help if no arguments given
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    global VERBOSE
    VERBOSE = 0
    if args.verbose:
        VERBOSE = args.verbose
        print_verbose("Verbose level {} active - dumping info to stderr".format(VERBOSE), 1)
        print_verbose("{} - {}".format(NAME, VERSION), 1)
        print_verbose("arg list: {}".format(args), 1)

    if args.version:
        sys.stderr.write("{} - {}\n".format(NAME, VERSION))
        sys.exit(1)

    r1_found = False
    r2_found = False
    name1 = ""
    name2 = ""
    seq1 = ""
    seq2 = ""
    with open(args.ref1, 'rt') as f:
        for l in f:
            if l[0] == ">":
                if r1_found:
                    print_err("More than one sequence found in ref1")
                    sys.exit()
                r1_found = True
                name1 = l.strip("\n")
            else:
                ln = l.strip("\n")
                seq1 = seq1 + ln.strip('"')

    with open(args.ref2, 'rt') as f:
        for l in f:
            if l[0] == ">":
                if r2_found:
                    print_err("More than one sequence found in ref2")
                    sys.exit()
                r2_found = True
                name2 = l.strip("\n")
            else:
                ln = l.strip("\n")
                seq2 = seq2 + ln.strip('"')


    print("ref1 length", len(seq1), sep="\t")
    print("ref2 length", len(seq2), sep="\t")
    result = edlib.align(seq1.upper(), seq2.upper(), task = "path")
    print(result)
    print("\n")
    nice = edlib.getNiceAlignment(result, seq1.upper(), seq2.upper())
    # print("\n".join(nice.values()))
    p = 0
    for i in range(0,len(nice["query_aligned"]), 80):
        print(nice["query_aligned"][p:i])
        print(nice["matched_aligned"][p:i])
        print(nice["target_aligned"][p:i])
        p = i



if __name__ == '__main__':
    main()
