from _classes import CardList, os, re
import random
from datetime import datetime 

class Quiz:
    def __init__(self, resources_dir = None) -> None:
        self.__cardlist = CardList(resources_dir)
        
        self.__questions_per_quiz = \
            int(input("How many questions do you want to have? (Max: " + str(len(self.__cardlist.cards_list)) + ") "))
        while type(self.__questions_per_quiz) != int and self.__questions_per_quiz > len(self.__cardlist.cards_list):
            self.__questions_per_quiz = \
                int(input("Please pick a NUMBER. (Max: " + str(len(self.__cardlist.cards_list)) + ")"))

        
        self.__show_answer_immediately = \
            input("Do you want to have the answer shown immediately after you respond?\n(If not, you will be shown a score at the end and a file will be generated with all of your answers, highlighting the wrong ones.)[y/N] ")

        if self.__show_answer_immediately == "":  # if only Enter was pressed
            self.__show_answer_immediately = "n"  # default to n

        self.__show_answer_immediately = self.__show_answer_immediately.lower()
        while self.__show_answer_immediately != "n" and self.__show_answer_immediately != "y":
            self.__show_answer_immediately = \
                input("Please pick between 'y'(yes) or 'n'(no): ")
            self.__show_answer_immediately = self.__show_answer_immediately.lower()
        
        self.quiz_cards = self.__generate_quiz()
    

    def __generate_quiz(self) -> list:
        random.shuffle(self.__cardlist.cards_list)
        return self.__cardlist.cards_list[:self.__questions_per_quiz]


    def __clear(self):
        print("")  # get a new empty line
        # for windows
        if os.name == 'nt':
            _ = os.system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = os.system('clear')    


    def start_quiz(self):
        self.__clear()

        correct_answers = 0

        filename = re.sub(" ", "_", str(datetime.now())).split(".")[0]  # remove the miliseconds as they were delimited by '.'
        filename = re.sub(":", "-", filename)  # remove ':' as they are a special char on Windows.. 
        filename += ".txt"
        wrong_answers_file = open(filename, "w")  # file where the wrong answers will be written to

        print("Your quiz starts now. Please enter one single character, coresponding to the answers (A,B,C or D). Answers are NOT case sensitive, so response 'b' is good if 'B' is the correct answer.\n")
        input("Press Enter to continue..")

        for card in self.quiz_cards:
            print("")
            print(card.question_number + " " + card.question)
            print("-" * 40)
            for ans in card.answers:
                print(ans)
            print("-" * 40)
            your_answer = ""
            while your_answer.upper() not in ['A', 'B', 'C', 'D']:
                your_answer = input("Your answer: ")

            if your_answer.upper() == card.correct_answer:
                correct_answers += 1
            else:
                # write to the wrong answer to the file
                wrong_answers_file.write(card.question_number + " " + card.question + "\n")
                wrong_answers_file.write("-" * 40 + "\n")
                for ans in card.answers:
                    wrong_answers_file.write(ans + "\n")
                wrong_answers_file.write("Your answer: " + your_answer.upper() + "\n")
                wrong_answers_file.write("Correct answer: " + card.correct_answer + "\n")
                wrong_answers_file.write("-" * 40 + "\n")
            
            if self.__show_answer_immediately == "y":
                print("Correct answer: ", card.correct_answer)
                input("Press Enter to continue..")
            
        
        print("=^=" * 40)
        print("The quiz is DONE! Good job!")
        print("Your score: " + str(correct_answers) + "/" + str(self.__questions_per_quiz))