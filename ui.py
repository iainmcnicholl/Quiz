from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        #link quiz brain from main to ui, :QuizBrain ensures only correct data type is accepted, quizbrain object
        self.quiz = quiz_brain
        #root window
        self.window = Tk()
        #theme constants
        self.theme_colour = "#375362"
        self.true_image = PhotoImage(file=".\images\\true.png")
        self.false_image = PhotoImage(file=".\images\\false.png")
        self.window.title("Quizzy Rascal")
        self.font_setup = ("arial", "16","italic")
        #window and widget setup
        self.window.config(padx=20, pady=20, bg=self.theme_colour)
        self.canvas = Canvas(bg="white", highlightthickness=0, width=300, height=250)
        self.question_text = self.canvas.create_text(150,
                                125,
                                text="This is a test text",
                                width=280,font=self.font_setup,
                                fill=self.theme_colour)
        self.true_button = Button(image=self.true_image, bd=0, highlightthickness=0, relief="flat", command=self.true_answer)
        self.false_button = Button(image=self.false_image, bd=0, highlightthickness=0, relief="flat",command=self.false_answer)
        self.score_label = Label(text=f"Score: {self.quiz.score}",
                                 fg="white",
                                 bg=self.theme_colour,
                                 font="arial")
        #widget positioning
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)
        self.score_label.grid(column=1, row=0)

        self.get_next_ques()

        self.window.mainloop()

    def get_next_ques(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"That is the end of the quiz, your score was {self.quiz.score} / 10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
       self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_ques)


