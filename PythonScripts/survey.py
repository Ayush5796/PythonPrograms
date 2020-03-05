class AnonymousSurvey():

    def __init__(self, question):
        self.question = question
        self.responses = []

    
    def show_question(self):
        "Show the Survey question"
        print(self.question)

    
    def store_response(self, new_response):
        "Stores the response of the user"
        self.responses.append(new_response)
    

    def show_results(self):
        "Shows the result of the survey"
        for res in self.responses:
            print("-" + res)