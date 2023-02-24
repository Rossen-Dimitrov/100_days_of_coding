class QuizBrain:
    """Entire quiz logic"""
    def __init__(self, questions_list: list):
        self.questions_list = questions_list
        self.idx = 0
        self.score = 0

    def is_next_question(self):
        return self.idx < len(self.questions_list)

    def next_question(self):
        cur_question = self.questions_list[self.idx]
        self.idx += 1
        print(f'Q.{self.idx}: "{cur_question.text}" True/False')
        answer = input("Type your answer here: ")
        self.check_answer(answer, cur_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"Correct")
        else:
            print(f"Wrong")

        print(f"Current score is {self.score}/{self.idx}")
        print()
