class QuizBrain:
    def __init__(self, questions, question_number=0):
        self.questions = questions
        self.question_number = question_number
        self.score = 0

    def next_question(self):
        question_text = self.questions[self.question_number].text
        user_answer = input(
            f"Q.{self.question_number + 1}: {question_text} (True / False)? "
        )
        self.check_answer(user_answer)
        self.question_number += 1
        print("\n")
        if len(self.questions) == self.question_number:
            self.print_final_score()

    def print_score(self):
        print(f"Your score is: {self.score} / {self.question_number + 1}")

    def check_answer(self, user_answer):
        question_answer = self.questions[self.question_number].answer
        if user_answer.lower() == question_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer was {question_answer}")
        self.print_score()

    def still_has_questions(self):
        return self.question_number + 1 <= len(self.questions)

    def print_final_score(self):
        print("\n")
        print("You completed the quiz.")
        print(f"Your final score is: {self.score}")
