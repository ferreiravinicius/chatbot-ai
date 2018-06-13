from flask import Flask, render_template, request
from bot import delphos

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    text = request.args.get('msg')
    return str(delphos.get_response(text))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)