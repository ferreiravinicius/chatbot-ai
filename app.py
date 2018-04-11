from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

alfonse = ChatBot(
    "Alfonse", 
    trainer="chatterbot.trainers.ListTrainer",
    storage_adapter="chatterbot.storage.SQLStorageAdapter"
    )

alfonse.train([
    "Qual é a primeira lei de Newton?",
    "Lei da Inércia, diz que a tendência dos corpos, quando nenhuma força é exercida sobre eles, é permanecer em seu estado natural, ou seja, repouso ou movimento retilíneo e uniforme. É por isso que quando o motorista freia o ônibus bruscamente e você está em pé, você quase cai no colo dele.",
    "Quem é Isaac Newton?",
    "Isaac Newton foi um cientista inglês do séc. XVII que formulou as leis da mecânica clássica.",
    "Qual é a segunda lei de Newton?",
    "A Segunda Lei de Newton diz que a força resultante que age sobre um corpo deve ser igual ao produto da massa do corpo por sua aceleração. De acordo com a Segunda Lei de Newton: “A força resultante que atua sobre um corpo é proporcional ao produto da massa pela aceleração por ele adquirida. ” É por isso que o Indiana Jones sai correndo para não ser esmagado pela pedrona."
])

#alfonse.set_trainer(ChatterBotCorpusTrainer)
#alfonse.train("chatterbot.corpus.portuguese")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(alfonse.get_response(userText))


if __name__ == "__main__":
    app.run()