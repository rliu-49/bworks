#!/usr/local/bin/python3
#Using Python Version 2.7.3
#module used to do regular expressions
import re
import hashlib
 
#replace string with wireshark output
#string = 'username="u1rliuEnt1grp1"  , realm="as2-syd-vm7"  , cnonce="6b8b4567"  , nc=00000001  ,qop=auth  ,uri="sip:10.66.82.12:5060"  ,nonce="BroadWorksXjnv58mfeT8nj820BW"  ,response="fc10f8c59598a279ba62b2660e9fa991"'
#string = 'username="3332017000" ,realm="as2-syd-vm7" ,cnonce="6b8b4567" ,nc=00000001 ,qop=auth ,uri="sip:10.66.82.12:5060" ,nonce="BroadWorksXjw8khpxeTjskhjtBW" ,response="ed7cbcdeddab06f17941b3da2d5390ed" ,algorithm=MD5'
string = 'username=N2782855R ,realm="tcc.com" ,nonce="BroadWorksXk6fmrx4aTh2fvkjBW" ,uri="sip:+61385999817@tcc-nsw1-tcc-cp.tipt.telstra.com:5060" ,response="337a31ee2544258cd127c4ab73a0f999" , algorithm=MD5 , cnonce="2369021178", qop=auth ,nc=00000001 '
#string = 'username="voip18549875" ,realm="BroadWorks" ,nonce="BroadWorksXjvxb66yhTs79l50BW" ,uri="sip:dodovoip.com.au" ,response="3c1c56c5423e4b26b6f617a458abc8e6" ,algorithm=MD5 ,nc=00000201 ,qop=auth ,cnonce="4c79d80a"'
#string='Authorization: Digest username="4072614331", realm="bt.voipdnsservers.com", algorithm=MD5, uri="sip:bt.voipdnsservers.com", nonce="BroadWorksXjnrrdy2wTci10c5BW", response="455eb7d75eae816042c8a6802bec0cbc", qop=auth, cnonce="5090e6fe", nc=00000001'
#Prompt to get user input
#password_File = raw_input("Password File Path: ")
s1 = string.replace('\"','').replace(',','')

print("string=" + s1)
text = 'foo = fred , name="rliu" ,username="u1rliuEnt1grp1", realm="as2-syd-vm7"' 
pattern = re.compile(r'(\S+) \s* = \s* ( [^\s"]+ | "[^\s"]+" \s* )', flags = re.X)
#pattern = re.compile(r'\w+')
matches = pattern.finditer(s1)

param = []
val = []

for match in matches:
        print(match)
        param.append(match.group(1))
        val.append(match.group(2))
        print(match.group(1) + "-> " + match.group(2))
        
print(param)
print(val)

pairs = { name: val for name, val in zip(param,val)}
pairs['password'] = 'Rvyqnllf9'
pairs['method'] = 'INVITE'
print(pairs)

print('username=' + pairs['username'] + "realm=" + pairs['realm'])

#password = '123456'
password='Rvyqnllf9'
print(type(password))
#username = pairs['username'].strip().strip('\"')
#print(type(username))
#realm = pairs['realm'].strip().strip('\"')

md = hashlib.md5()
#md.update(username.encode())
#print( type(username))
#print(md.hexdigest())
#ha2 = hashlib.md5("foo".encode())
ha1_str = "{username}:{realm}:{password}".format(**pairs)
ha2_str = "{method}:{uri}".format(**pairs)

print(ha1_str)
print(ha2_str)

ha1 = hashlib.md5(ha1_str.encode()).hexdigest()
ha2 = hashlib.md5(ha2_str.encode()).hexdigest()

#ha1 = hashlib.md5(b'u1rliuEnt1grp1:as2-syd-vm7:123456').hexdigest()
print(type(ha1))
print(ha1)
print(ha2)

mid = "{nonce}:{nc}:{cnonce}:{qop}".format(**pairs)
print(mid)

#fin_str = ha1 + ':' + mid + ':' + ha2
fin_str = "{ha1}:{mid}:{ha2}".format(ha1=ha1, mid=mid, ha2=ha2)
print(fin_str)
#fin_hash = "{ha1}:{mid}:{ha2}".format()
response = hashlib.md5(fin_str.encode()).hexdigest()
print(response)
print(pairs['response'])