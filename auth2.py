import hashlib

def get_hash(str):
    return hashlib.md5(str.encode('utf-8')).hexdigest()

s1 = '3332017002:as1-syd-r23.cisco.com:Dopegang1!'
h = get_hash(s1)
print(h)