from survey import AnonymousSurvey

#Define a question for the survey
question = "Which language did you first learned??"
my_survey = AnonymousSurvey(question)

#Show the question for the survey
my_survey.show_question()

#Collect the response
print("Enter 'q' when you want to quit!!!")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    else:
        my_survey.store_response(response)


my_survey.show_results()
