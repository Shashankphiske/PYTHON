from quizdata import question_data
from question_class import Question
from quiz_brain import quizbrain

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
initialize = quizbrain(question_bank)

while initialize.stillquestions():
    initialize.nextquestion()
print("you have completed the quiz")
print(f"Your current score is {initialize.score}/{initialize.question_num}")    



 
