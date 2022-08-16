"""Create a method called next_question() - needs to retrieve the item at the current question_number from the question_list.
 Use the input() to show the user the question text and ask for the users answer."""

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
