from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

alfonse = ChatBot("Alfonse", storage_adapter="chatterbot.storage.SQLStorageAdapter")

alfonse.set_trainer(ChatterBotCorpusTrainer)
alfonse.train("chatterbot.corpus.portuguese")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(alfonse.get_response(userText))


if __name__ == "__main__":
    app.run(host='0.0.0.0')