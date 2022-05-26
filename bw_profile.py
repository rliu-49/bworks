import requests
import json

#USER='3332017001@as1-r23-syd.cisco.com'
#HOST='xsp1-r23-syd.cisco.com'
USER='3332017001@r21sp1syd.bstac.net'
HOST='xsp1-r21-syd.cisco.com'
url=f'https://{HOST}/authService/token/{USER}?format=json'
password="123456"
headers = { 'X-BroadWorks-Protocol-Version': '1.0', 'Content-Type': 'application/json' }
resp = requests.get(url, verify = False, 
        headers = headers, auth = (USER, password))

print(resp.text, resp.status_code)
token_map = resp.json()
access_token =  token_map['token']['bearer']
print(f'access_token={access_token}')
url2 = f'https://{HOST}/com.broadsoft.xsi-actions/v2.0/user/{USER}/profile?format=json'


headers = {  'Content-Type': 'application/json; ; charset=UTF-8', 'Authorization': f'Bearer {access_token}' }
resp = requests.get(url2, verify = False, 
        headers = headers)

if resp.status_code != 200: 
    print(resp.status_code)
    exit

profile = resp.json()
#print("profile=",profile)
json_dict = json.loads(resp.text)

print(json_dict['Profile']['details']['userId']['$'])
print(json_dict)
