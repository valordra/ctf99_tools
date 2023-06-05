from flask import Flask, render_template, request, render_template_string
from base64 import b64encode, b64decode

app = Flask(__name__)
BLACKLIST = ["class", "mro", "request", ".", "[", "]"]

@app.route("/", methods=['GET'])
def home():
    html = """
    <html>
        <head><title>Pencarian Super</title></head>
        <body>
            <form>
                <input type='text' name='q' required>
                <input type='submit' value='Cari'>
            </form>
            <p></p>
        </body>
    </html>
    """
    srckey = request.args.get('q', "")
    for k in BLACKLIST:
        if srckey.find(k) != -1:
            return render_template_string(html)
    if srckey:
        html = html.replace("<title>", "<title>" + srckey + " | ")
        html = html.replace("<p>", "<p>Ya ndak tahu, kok tanya saia...")
    return render_template_string(html)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
