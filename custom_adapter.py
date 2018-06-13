from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from unidecode import unidecode
import secrets

intents = {
    'primeira_lei_newton' : {
        'required': ['primeira', 'lei', 'newton'],
        'optional': [],
        'answer': "teste_newton_1"
    },
    'segunda_lei_newton' : {
        'required': ['segunda', 'lei', 'newton'],
        'optional': [],
        'answer': "teste_newton_2"
    },
    'segunda_lei_kepler' : {
        'required': ['segunda', 'lei', 'kepler'],
        'optional': [],
        'answer': "teste_kepler_2"
    },
}

class CustomAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        super(CustomAdapter, self).__init__(**kwargs)

    def can_process(self, statement):
        return True

    def process(self, statement):
        text = self.sanitize(statement.text)

        for intent, data in intents.items():
            if all(self.match(text, word) for word in data.get('required')):
                return Statement(data.get('answer'))

        random_text = secrets.choice([
            "Não consegui encontrar sobre este assunto. Tente ser mais específico citando o nome do cientista e a teoria que deseja.",
            "Não consegui entender, parece incompleto. Tente acrescentar o nome do cientista.",
            "Você precisa ser um pouco mais epecífico, talvez dizer o nome do cientista junto com a teoria ajude."
        ])

        response = Statement(random_text)
        response.confidence = 0
        return response

    def sanitize(self, text):
        return unidecode(text.lower())

    def match(self, text, word):
        import re
        return word in re.split(' |-', text)