from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_bank = []
for question in question_data:
    entry = Question(question["text"], question['answer'])
    question_bank.append(entry)

quiz = Quiz(question_bank)

while quiz.stillhasquestions():
    quiz.next_question()

print("You've completed the Quiz!")
print(f"Your final score was : {quiz.score}/{quiz.question_number}")