from chatterbot import ChatBot
from training import treino, padrao, cumprimento

delphos = ChatBot(
    "Delphos", 
    trainer="chatterbot.trainers.ListTrainer",
    logic_adapters=[
        "custom_adapter.CustomAdapter"
    ],
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database='./db.sqlite3'
    )

# def treinar(entrada): 
#     if isinstance(entrada, dict):
#         for lista in entrada.values():
#             delphos.train(lista)
#     else:
#         delphos.train(entrada)

# treinar(treino)
# treinar(padrao)
# treinar(cumprimento)

