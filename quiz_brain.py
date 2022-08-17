class QuizBrain:

    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.q_num < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.q_num]
        self.q_num += 1
        user_answer = input(f"Q.{self.q_num}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print(f"That's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Score: {self.score}/{self.q_num}")
        print("\n")





