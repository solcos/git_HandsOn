# Script that computes, given a DNA or RNA sequence, the percentage of each nucleotide.

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()      

if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq): # search in the sequence if there is a T
        if not re.search('U',args.seq): # search if it is not a U
            print ('The sequence is DNA') #Print the result
            A=(args.seq.count('A')/len(args.seq))*100
            C=(args.seq.count('C')/len(args.seq))*100
            G=(args.seq.count('G')/len(args.seq))*100
            T=(args.seq.count('T')/len(args.seq))*100
            print (f'Looking for percentage of the nucleotides of DNA: "{round(A,2)}"% of As, "{round(C,2)}"% of Cs, "{round(G,2)}"% of Gs, "{round(T,2)}" % of Ts')
        else:
            print ('The sequence is incorrect')
    elif re.search('U', args.seq): # Search if there is a U
        if not re.search('T',args.seq): # Search if there is not a T too
            print ('The sequence is RNA')
            A=(args.seq.count('A')/len(args.seq))*100
            C=(args.seq.count('C')/len(args.seq))*100
            G=(args.seq.count('G')/len(args.seq))*100
            U=(args.seq.count('U')/len(args.seq))*100
            print (f'Looking for percentage of the nucleotides of RNA: "{round(A,2)}"% of As, "{round(C,2)}"% of Cs, "{round(G,2)}"% of Gs, "{round(U,2)}" % of Us')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

