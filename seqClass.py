
#!/usr/bin/env python

# Import packages
import sys, re
from argparse import ArgumentParser

# Set description an arguments
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# Select by length
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# Main function
args.seq = args.seq.upper()
# Select only the sequences with the following nucleotids
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq): # search in the sequence if there is a T
        if not re.search('U',args.seq): # search if it is not a U
            print ('The sequence is DNA') #Print the result
        else:
            print ('The sequence is incorrect')
    elif re.search('U', args.seq): # Search if there is a U
        if not re.search('T',args.seq): # Search if there is not a T too
            print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

# Return
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND THE MOTIF")
