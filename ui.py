from tkinter import *
from quiz_brain import QuizBrain

# -------------- CONSTANTS -------------- #
THEME_COLOR = "#375362"
FONT_NAME = "Arial"


# -------------- UI CLASS -------------- #
class Interface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window:
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Canvas:
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="TEST", font=(FONT_NAME, 18, "bold"),
                                                     fill=THEME_COLOR, width=280)
        # Buttons:
        self.cross_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.cross_img, bg=THEME_COLOR, relief=GROOVE, padx=20, pady=20,
                                   command=self.false_answer)
        self.check_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.check_img, bg=THEME_COLOR, relief=GROOVE, padx=20, pady=20,
                                  command=self.true_answer)
        # Labels:
        self.score_label = Label(text="SCORE: 0", bg=THEME_COLOR, fg="white", font=(FONT_NAME, 8, "italic"))
        # Positioning:
        self.score_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        # Functions:
        self.get_next_question()
        # MainLoop
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        user_score = self.quiz.check_answer(user_answer="True")
        self.score_label.config(text=f"SCORE: {user_score[0]}/{user_score[1]}")
        self.get_next_question()

    def false_answer(self):
        user_score = self.quiz.check_answer(user_answer="False")
        self.score_label.config(text=f"SCORE: {user_score[0]}/{user_score[1]}")
        self.get_next_question()
