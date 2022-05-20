import requests

USER='3332017001@as1-r23-syd.cisco.com'
HOST='xsp1-r23-syd.cisco.com'
url=f'https://{HOST}/authService/token/{USER}'
password="Password1!"
headers = { 'X-BroadWorks-Protocol-Version': '1.0' }
resp = requests.get(url, verify = False, 
        headers = headers, auth = (USER, password))

print(resp.text, resp.status_code)
