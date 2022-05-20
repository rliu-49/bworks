#!/usr/local/bin/python3

import xml.etree.ElementTree as ET

tree = ET.parse('/users/riliu2/Documents/callhistoryEvent.xml')
root = tree.getroot()

h = {'ff', 'bar'}
print(h)

for child in root:
    print(child.tag[33:], child.text)
    
