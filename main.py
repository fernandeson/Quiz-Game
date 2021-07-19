from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import Interface


# Converting data FROM data.py/question_data[] to OBJECTS
question_bank = []
for item in question_data:
    new_question = Question(q_text=item["question"], q_answer=item["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = Interface(quiz)
