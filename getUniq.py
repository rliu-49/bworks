#!/usr/local/bin/python3

import re, sys, argparse
import ipaddress as ip

## Global variables
callids = set()
username = {}
user = ''
flag = False



def main():
    descStr = """
    Just getting user data
    """
    parser = argparse.ArgumentParser(description=descStr)
    # group is for exclusive arguments
    parser.add_argument('--infile', nargs='?', dest='infile', default=sys.stdin, required=True, help='XSLog file to parse.')
    parser.add_argument('--outfile', nargs='?', dest='outfile', default=sys.stdout, required=True, help='Output file to write hashed text.')

    # Start to parse the arguments
    args = parser.parse_args()
    user = ''
    user_agent = ''
    authuser = ''
    flag = False

    print("+----------------------------------------+")
    print("\t Starting the XSLog sanitizer.")
    print("+----------------------------------------+")
    if args.infile:
        infile = args.infile
        print('Input:\t\t', infile)
    if args.outfile:
        outfile = args.outfile
        print('Output:\t\t', outfile)
    print("+----------------------------------------+")
    print("\t End of input parameters")
    print("+----------------------------------------+")

    with open(infile, 'r') as file:
        output = file.readlines()
        linenum = 0
        for line in output:
            if '403 Authentication Failure' in line:
                print('auth fail')
                if 'Call-ID' in output[linenum+4]:
                    cid = output[linenum+4].strip().split(':')
                    print('callId=',cid)
                    callids.add(str(cid[1]))
            linenum += 1
    ## Here we just parse the file again and store the user agent, user-name, auth user.
    authuser = user_agent = num = ""
    print(callids)
    with open(infile, 'r') as file:
        output = file.readlines()
        linenum = 0
        for line in output:
            if re.match('^2021', line):
                num = linenum+1
                if flag:
                    username[user] = ((num, authuser, user_agent))
                    flag = False
                    authuser = user_agent = ""
                    a = line.strip().split(' | ')
                    user = a[4]
                    print('adding to username=', a)
            elif re.search('call-id', line, re.IGNORECASE):
                a = line.strip().split(':')
                print('a= ', a[1])
                if a[1] in callids:
                    print('found callid')
                    flag = True
                else:
                    flag = False
            elif re.search('user-agent', line, re.IGNORECASE):
                a = line.strip().split(':')
                user_agent = a[1]
            elif re.search('^authorization', line, re.IGNORECASE):
                a = line.strip().split(',')
                for v in a:
                    if re.search('username=', v, re.IGNORECASE):
                        x = v.split('=')
                        x[1] = x[1].replace('"', '')
                        authuser = x[1].replace(',', '')
            if (linenum % 100000 == 0):
                print('Working on linenum: ', linenum)
            linenum += 1

    with open(outfile, 'w') as outf:
        i = 1
        outf.write('Username      Linenumber      User-Agent      Authuser\n')
        outf.write('------------------------------------------------------\n')
        for key in sorted(username):
            if (i / 100 == 0):
                outf.write('Username      Linenumber      User-Agent      Authuser\n')
                outf.write('------------------------------------------------------\n')
            outf.write(key)
            outf.write('\n')
            for c in username[key]:
                outf.write(str(c))
                outf.write(' -- ')
            i += 1

if __name__ == '__main__':
    main()
