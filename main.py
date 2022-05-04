from bs4 import BeautifulSoup as bs
import os 

RES_DIR = "./res"  # directory of resources

class Card:
    """ Represents a structure that contains one question with
        4 answers and a correct answer. 

        To not be confused with a Page, which would hold all the questions
        and answers on a HTML page.
    """
    def __init__(self, _questions, _answers, _correct_answer) -> None:
        self.question = _questions
        self.answers = _answers
        self.correct_answer = _correct_answer


class Quiz:
    """ Represents a structure that holds a list of Cards """
    def __init__(self) -> None:
        self.soup_list = self.__init_soup(self.__get_list_of_html())
        self.cards_list = [] 

        for soup in self.soup_list:
            questions = self.__get_questions(soup)
            answers = ["This", "that", "Thisc", "Thisd"]
            correct_answer = "D"

            # This is incorrect as this creates a page(4 questions, 16 ans etc), not a card
            self.cards_list.append(Card(questions, answers, correct_answer))


    def __get_list_of_html(self) -> list:
        """ Iterates through directory where HTML files are and
            returns their names
        """
        html = []
        for file in os.listdir(RES_DIR):
            _ = os.path.join(RES_DIR, file)
            if os.path.isfile(_):
                html.append(_)
        return html  # order is irrelevant


    def __init_soup(self, html_list: list):
        """ Creates a list of soups so that we can easily parse each of them """
        soup_list = [] 
        for html_file in html_list:
            with open(html_file, "r", encoding="utf8") as fhandler:
                soup = bs(fhandler.read(), "html.parser")
                soup_list.append(soup)
        return soup_list


    def __get_questions(self, soup) -> list:
        """ Returns the 4 questions available in this soup as text.
            This returns all the questions on a PAGE.
         """
        qbodies = soup.find_all("div", attrs={'class': "question-body"})

        questions = []
        for body in qbodies:
            questions.append(body.find("p", attrs={'class': "card-text"}).text)
        return questions

    def __get_answers(self, soup) -> list:

    def get_questions(self) -> list:
        questions = []
        for card in self.cards_list:
            questions.append(card.question)
        return questions 


if __name__ == "__main__":
    quiz = Quiz()
    print(quiz.get_questions())