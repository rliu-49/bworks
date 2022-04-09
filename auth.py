import hashlib

def get_hash(str):
    print('string = ',str)
    print(hashlib.md5(str.encode('utf8')).hexdigest())
    return hashlib.md5(str.encode('utf8')).hexdigest()

def calc_response(pairs):
 
    ha1_str = "{username}:{realm}:{password}".format(**pairs)
    #ha1_str = '3332017002:as1-r23-syd.cisco.com:Dopegang1!'
    print('ha1_str = ', ha1_str)
    #ha1 = get_hash('3332017002:as1-r23-syd.cisco.com:Dopegang1!')
    ha1 = get_hash(ha1_str)
    print('ha1 =', ha1, "password =", pairs['password'] )
    mid = "{nonce}:{nc}:{cnonce}:{qop}".format(**pairs)

    ha2_str = "{method}:{uri}".format(**pairs)
    print(f'ha2str = {ha2_str}')
    ha2 = get_hash(ha2_str)
    fin_str = f'{ha1}:{mid}:{ha2}'
    print(fin_str)
    '''response = MD5(HA1:nonce:nonceCount:cnonce:qop:HA2)'''
    return get_hash(fin_str)

def parse_auth_header():
#auth_header='Authorization: Digest username="3332017001", realm="as1-r23-syd.cisco.com", nonce="BroadWorksXl1ocj9glT33ns0fBW", uri="sip:as1-r23-syd.cisco.com", response="32a98f82af209e5cdd986b5b5571a8de", algorithm=MD5, cnonce="XOmVefBe26FB3TsKOgWjZJRFJYsmPjj6", qop=auth, nc=00000001'
    auth_header='Authorization: Digest username="3332017002", realm="as1-r23-syd.cisco.com", nonce="BroadWorksXl1pvf7hdTycxwdcBW", uri="sip:as1-r23-syd.cisco.com", response="22cdda4444a2d8edda6f9943b4955bad", algorithm=MD5, cnonce="c4d3d62bdd4b6b78a655a6d", qop=auth, nc=00000002'
    auth_header2 = auth_header.replace(',' ,'' ,-1).replace('"', '', -1)
    pairs = auth_header2.split()

    auth = dict()

    for word in pairs[2:]:
        print(word)
        auth_param = word.split('=')
        k = auth_param[0]
        v = auth_param[1]
        print(auth_param[1])
        auth[k]= v
    auth["password"] = "Dopegang1!"
    auth["method"] = "REGISTER"

    print(auth)
    res = calc_response(auth)
    print(f'res={res}')

if __name__ == '__main__':
    print(hashlib.md5('3332017002:as2-r23-syd.cisco.com:Dopegang1!'.encode('utf-8')).hexdigest())
    s1 = '3332017002:as2-r23-syd.cisco.com:Dopegang1!'
    get_hash('3332017002:as2-r23-syd.cisco.com:Dopegang1!')
    get_hash(s1)
    
    parse_auth_header()
        






