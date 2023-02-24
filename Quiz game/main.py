from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions_bank = []
quiz = QuizBrain(questions_bank)

for question in question_data:
    q_text = question['text']
    q_answer = question['answer']
    cur_question = Question(q_text, q_answer)
    questions_bank.append(cur_question)

while quiz.is_next_question():
    quiz.next_question()


