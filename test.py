#!/usr/local/bin/python3
import sys
import re

p = re.compile('channel')


for line in sys.stdin.readlines():
    m = p.match(line)
    if m:
        continue
    fld = line.split(' ')

    u = fld[6].split('/')
    print(fld[3], fld[5], u[1], u[2], u[3], u[4])

    # print $Fld4, $Fld6, $u[(2)-1], $u[(3)-1], $u[(4)-1], $u[(5)-1];
