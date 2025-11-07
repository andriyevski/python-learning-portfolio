class AnonymousSurvey():
    """docstring for AnonymousSurvey."""

    def __init__(self, question):
        """ Save question and ready to save answer """
        self.question = question
        self.responses = []

    def show_question(self):
        """ print question """
        print(self.question)

    def store_response(self, new_response):
        """ save one your question """
        self.responses.append(new_response)

    def show_result(self):
        """ Print all taked answers """
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
