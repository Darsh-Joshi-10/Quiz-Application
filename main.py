#Quiz Application
import tkinter as tk
from tkinter import messagebox

class QuizApplication:
    def __init__(self, master):
        self.master = master
        self.score = 0
        self.current_question_index = 0

        self.questions = [
            {
                "question": "What is the capital of India?",
                "options": ["Paris", "London", "Berlin", "Delhi"],
                "correct_option": 3
            },
            {
                "question": "What is the capital of Tamil Nadu?",
                "options": ["Chennai", "Tambaram", "Gudvancherry", "Avadi"],
                "correct_option": 0
            },
            {
                "question": "What is the capital of Gujarat?",
                "options": ["Ahmedabad", "Gandhinagar", "Surat", "Vadodara"],
                "correct_option": 0
            },
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Delhi"],
                "correct_option": 0
            },
            {
                "question": "What is the capital of Maharashtra?",
                "options": ["Mumbai", "Borivali", "Lokhandvala", "Sea link"],
                "correct_option": 0
            }
        ]
        self.question_label = tk.Label(master, text='', font=("Arial", 12))
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(master, text='', font=("Arial", 10), width=30, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.next_question()

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question_info = self.questions[self.current_question_index]
            self.question_label.config(text=question_info["question"])

            for i in range(4):
                self.option_buttons[i].config(text=question_info["options"][i])

        else:
            self.show_result()

    def check_answer(self, selected_option):
        correct_option = self.questions[self.current_question_index]["correct_option"]
        if selected_option == correct_option:
            self.score += 1

        self.current_question_index += 1
        self.next_question()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"You scored {self.score}/{len(self.questions)}")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quiz Application")
    app = QuizApplication(root)
    root.mainloop()
