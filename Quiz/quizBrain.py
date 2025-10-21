class QuizBrain:
    def __init__ (self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def stillHasQuestions(self):
        return self.question_number < len(self.question_list)
    
    def checkAnswer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Current score is: {self.score}/{self.question_number}.")
        print("\n" * 5)
    
    def nextQuestion(self):
        qAndA = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number}: {qAndA.text} (True/False)?: ")
        self.checkAnswer(answer, self.question_list[self.question_number].answer)
        self.question_number += 1