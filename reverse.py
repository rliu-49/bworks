#!/usr/bin/python

import re
import sys
import getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'order.it -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'order.it -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    with open(inputfile, 'r') as i:
        my_array = []
        logstatement = []
        file = i.readlines()
        for line in file:
            if re.match('^2021', line):
                if len(logstatement) > 1:
                    my_string = logstatement
                    my_array.append(my_string)
                    logstatement = []
                    logstatement.append(line)
                else:
                    logstatement.append(line)
            else:
                logstatement.append(line)

    with open(outputfile, 'w+') as o:
        while len(my_array) > 1:
            for i in my_array.pop():
                print('Writing: %s', i)
                o.write(i)
            o.write('\n')


if __name__ == "__main__":
    main(sys.argv[1:])
