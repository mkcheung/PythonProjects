from data import question_data
from question import Question
from quizBrain import QuizBrain

question_list = [];
for question in question_data:
    question_list.append(Question(question['text'], question['answer']))

qb = QuizBrain(question_list)

while qb.stillHasQuestions():
    qb.nextQuestion();

print("Quiz Completed!\n")
print(f"Your final score was: {qb.score}/{qb.question_number}")