class QuizGameSystem:
    def __init__(self):
        '''
        Initialize the game with instance
        Set the object by calling the get_class method
        '''
        self.questions = self.get_questions()

    def welcome_message(self):
        '''
        Display the welcome message
        '''
        print("Welcome to AskPython Quiz!!")

    def start_game(self, start = None):
        '''
        Question to start a game
        Parameters:
            start (string): This is the initialization answer by user

        bools:
        True if the user answered yes, False otherwise the user answered no
        '''
        while True:
            if start == None:
                start = input("Are you ready to play the Quiz? (yes/no) :").lower()

            if start == "yes":
                return True

            elif start == "no":
                print("See you next time!!")
                return False

            else:
                print("Invalid! Enter yes or no")
                start = None

    def get_questions(self):
        '''
        Return a list of questions
        '''
        return [
            {"question": "Question 1: What is your Favourite programming language?",
             "answer": "python"},
            {"question": "Question 2: Do you follow any author on AskPython?",
             "answer": "yes"},
            {"question": "Question 3: What is the name of your favourite website for learning Python?",
             "answer": "askpython"},
        ]

    def ask_question(self, question, correct_answer):
        '''
        Ask a question and return the correct or incorrect

        parameters:
        question (string): the answer user input to the question
        correct_answer (string): the correct answer to the question

        returns:
        return the point that user can get from the question
        '''
        answer = input(question)
        if answer == correct_answer:
            print("correct\n")
            return 1
        else:
            print("Wrong Answer :(\n")
            return 0

    def show_result(self, score, total):
        '''
        Show the result of the game
        Parameters:
            score (int):the score that user got from the game
            total (int):total number of questions

        return:
            mark(int): the percentage that the user got correct from the game
        '''
        print(f"Thank you for Playing this small quiz game, you attempted {score}, questions correctly!\n")
        mark = int((score / total) * 100)
        print("<<<<<Correct answers>>>>>")
        self.show_answer()
        print(f"Marks obtained: {mark}%\n")
        return mark

    def show_answer(self):
        '''
        Show all correct answers in the game
        '''
        count = 1
        for question in self.questions:
            answer = question["answer"]
            print(f"Question {count}:{answer}")
            count += 1
