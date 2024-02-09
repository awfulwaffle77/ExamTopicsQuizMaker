from io import TextIOWrapper
from _classes import CardList, os, re
import random
from datetime import datetime
import json
import textwrap

class Quiz:
    def __init__(self, resources_dir=None) -> None:
        self.__cardlist = CardList(resources_dir)
        self.__log_dirname = "quiz_logs"  # the name of the directory where the JSON files with quiz logs will be stored
        
        self.__init_questions_per_quiz()
        self.__init_show_answer_immediately()

        self.__create_logs_directory()

        self.quiz_logs = self.__generate_quiz_logs()

    def __init_questions_per_quiz(self):
        """
        Initialize the variable that shows how many questions should be shown in a quiz run
        """
        try:
            self.__questions_per_quiz = int(input("How many questions do you want to have? (Max: " + str(
                len(self.__cardlist.cards_list)) + ") "))

            while type(self.__questions_per_quiz) != int or self.__questions_per_quiz > len(
                    self.__cardlist.cards_list):
                self.__questions_per_quiz = int(input("Please pick a NUMBER. (Max: " + str(
                    len(self.__cardlist.cards_list)) + ")"))
        except:
            print("Defaulted to the max number of questions.")
            self.__questions_per_quiz = len(self.__cardlist.cards_list)

    def __init_show_answer_immediately(self):
        """
        Initializes the variable that decides if you want the correct answer shown after you respond
        """
        self.__show_answer_immediately = input(
            "Do you want to have the answer shown immediately after you respond?\n"
            "(If not, you will be shown a score at the end and a file will be generated with the wrong answers anyway.)[Y/n] ")

        if self.__show_answer_immediately == "":  # if only Enter was pressed
            self.__show_answer_immediately = "y"  # default to y

        self.__show_answer_immediately = self.__show_answer_immediately.lower()
        while self.__show_answer_immediately != "n" and self.__show_answer_immediately != "y":
            self.__show_answer_immediately = input("Please pick between 'y'(yes) or 'n'(no): ")
            self.__show_answer_immediately = self.__show_answer_immediately.lower()

    def __generate_quiz_logs(self) -> list:
        """
        Generate a list of dictionaries containing quiz data before the user answers the questions
        """
        random.shuffle(self.__cardlist.cards_list)

        quiz_logs = []
        for card in self.__cardlist.cards_list[:self.__questions_per_quiz]:
            quiz_logs.append({
                'question_number': card.question_number,
                'question': card.question,
                'answers': card.answers,
                'correct_answer': card.correct_answer,
                'user_response': None
            })

        return quiz_logs

    def __clear(self):
        """
        Clear the terminal window
        """
        print("")  # get a new empty line
        # for windows
        if os.name == 'nt':
            _ = os.system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = os.system('clear')

    def __create_logs_directory(self):
        try:
            os.mkdir(self.__log_dirname)
        except:
            print("Quiz logs directory already exists. Continuing..")

    def __init_answers_file(self) -> TextIOWrapper:
        """
        Initialize the filename with the current datetime, while omitting spaces and colon
        """
        filename = re.sub(" ", "_", str(datetime.now())).split(".")[0]  # remove the milliseconds as they were delimited by '.'
        filename = re.sub(":", "-", filename)  # remove ':' as they are a special char on Windows..
        filename += ".json"
        filename = os.path.join(self.__log_dirname, filename)
        quiz_log_file = open(filename, "w")  # file where the quiz log will be written to

        return quiz_log_file

    def start_quiz(self):
        """
        The main logic function for the quiz to run
        """
        self.__clear()

        print("Your quiz starts now. Please enter one single character, corresponding to the answers (A,B,C, or D). "
              "Answers are NOT case sensitive, so response 'b' is good if 'B' is the correct answer.\n")
        input("Press Enter to continue..")

        for index, quiz_log in enumerate(self.quiz_logs):
            print("")
            print(str(index + 1) + "/" + str(self.__questions_per_quiz))
            print(quiz_log['question_number'] + " " + textwrap.fill(text=quiz_log['question']))
            print("-" * 40)
            for ans in quiz_log['answers']:
                print(textwrap.fill(text=ans))
            print("-" * 40)

            your_answer = ""
            while your_answer.upper() not in ['A', 'B', 'C', 'D']:
                your_answer = input("Your answer: ")

            self.quiz_logs[index]['user_response'] = your_answer.upper()

            if self.__show_answer_immediately == "y":
                print("Correct answer: ", quiz_log['correct_answer'])
                input("Press Enter to continue..")

        quiz_log_file = self.__init_answers_file()
        json.dump(self.quiz_logs, quiz_log_file, indent=2)
        quiz_log_file.close()

        correct_answers = sum(1 for quiz_log in self.quiz_logs if
                              quiz_log['user_response'] == quiz_log['correct_answer'])
        print("=^=" * 40)
        print("The quiz is DONE! Good job!")
        print("Your score: " + str(correct_answers) + "/" + str(self.__questions_per_quiz))



