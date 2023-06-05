import requests
url = 'https://digilib.itb.ac.id/gdl/download/287431'
response = requests.get(url)
print(response.text)
print(response.content)