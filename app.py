from flask import Flask, render_template, request, redirect
import json
import string
import random
import os

app = Flask(__name__)

URLS_FILE = "urls.json"

# Create urls.json if not exists
if not os.path.exists(URLS_FILE):
    with open(URLS_FILE, "w") as f:
        json.dump({}, f)

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route("/", methods=["GET", "POST"])
def index():
    short_url = None

    if request.method == "POST":
        original_url = request.form["original_url"]

        with open(URLS_FILE, "r") as f:
            urls = json.load(f)

        short_code = generate_short_url()
        urls[short_code] = original_url

        with open(URLS_FILE, "w") as f:
            json.dump(urls, f)

        short_url = request.host_url + short_code

    return render_template("index.html", short_url=short_url)

@app.route("/<short_code>")
def redirect_url(short_code):
    with open(URLS_FILE, "r") as f:
        urls = json.load(f)

    original_url = urls.get(short_code)
    if original_url:
        return redirect(original_url)
    return "URL not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
