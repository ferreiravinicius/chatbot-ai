class Intent:

    def __init__(self, name, **kwargs):
        self.name = name
        self._questions = kwargs.get('questions', [])
        self._answers = kwargs.get('answers', [])
        self._required_keywords = kwargs.get('required', [])

    @classmethod
    def add_answer(self, text):
        self._answers.append(text)

    def add_question(self, text):
        self._questions.append(text)

    def add_required_keyword(self, text):
        self._required_keywords.append(text)

    @property
    def required_keywords(self):
        return self._required_keywords

    @required_keywords.setter
    def required_keywords(self, keywords):
        self._required_keywords = keywords