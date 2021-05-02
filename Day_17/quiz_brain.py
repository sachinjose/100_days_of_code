class Quiz:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def stillhasquestions(self):
        return self.question_number < len(self.question_list)


    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print('You are correct!')
            self.score+=1
        else:
            print("That's wrong")
            print(f"The correct answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number+1}")
        print("\n")

    def next_question(self):
        ans = input(f"Q{self.question_number+1} : {self.question_list[self.question_number].question} (True/False)? : ")
        self.check_answer(ans, self.question_list[self.question_number].answer)
        self.question_number += 1