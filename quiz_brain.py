class quizbrain:

    def __init__(self,q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0
    def stillquestions(self):
        return self.question_num < len(self.question_list)

    def nextquestion(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {current_question.text} (True/False)")
        self.checkanswer(user_answer,current_question.answer)

    def checkanswer(self,user_answer,correctanswer):
        if user_answer.lower() == correctanswer.lower():
            print("correct")
            self.score += 1
        else:
            print("wrong")
        print(f"The correct answer is {correctanswer}") 
        print(f"Your current score is {self.score}/{self.question_num}")  
        print("\n") 

