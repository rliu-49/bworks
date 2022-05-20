import hashlib
import sys
import getopt

def get_hash(str):
    return hashlib.md5(str.encode('utf-8')).hexdigest()

def main(argv):
    s1 = '3332017002:as1-syd-r23.cisco.com:Dopegang1!'
    h = get_hash(s1)
    print(h)

if __name__ == '__main__':
    main(sys.argv[1:])
    opts, args = getopt.getopt(sys.argv[1:],"hA:",["authheader"])
    print(opts, args)
    auth_header = ''
    for opt, arg in opts:
        if opt == '-h':
            print(f'-h ->{opt}:{arg}<-')
            sys.exit()
        elif opt in ("-A","auth header"):
            print(f'-A ->{opt}:{arg}<-')
            print(f'arg = {arg}')
            auth_header = arg
    print(auth_header)

    
        
