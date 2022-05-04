from bs4 import BeautifulSoup as bs
import os 

RES_DIR = "./res"  # directory of resources

class Page:
    """ Represnts a structure which holds all the questions and answers on a HTML page. """
    def __init__(self, _questions, _answers, _correct_answer) -> None:
        self.questions = _questions
        self.answers = _answers
        self.correct_answer = _correct_answer


class Quiz:
    """ Represents a structure that holds a list of Cards """
    def __init__(self) -> None:
        self.soup_list = self.__init_soup(self.__get_list_of_html())
        self.pages_list = [] 

        for soup in self.soup_list:
            questions = self.__get_questions(soup)
            answers = self.__get_answers(soup)
            correct_answer = self.__get_correct_answers(soup)

            self.pages_list.append(Page(questions, answers, correct_answer))


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
        qbodies = soup.find_all("div", attrs={'class': "question-body"})  # question body

        questions = []
        for body in qbodies:
            questions.append(body.find("p", attrs={'class': "card-text"}).text)
        return questions


    def __get_answers(self, soup) -> list:
        abody = soup.find_all("div", attrs={'class': "question-choices-container"})  # answers body

        answers = []
        for body in abody:
            set_of_answers = body.find_all("li", attrs={'class': "multi-choice-item"})  # answers on a card
            set_of_answers = [_.text for _ in set_of_answers]  # get rid of tags
            answers.append(set_of_answers)
        
        return answers


    def __get_correct_answers(self, soup) -> list:
        """ 
        Returns a list with the correct answers on the page

        As the "correct answer" stated by ExamTopics is usually wrong,
        the metric that is used here is to get the most popular (first) 
        answer from the progress bar (Community vote distribution bar)

        It appears that some questions (ex. #40) do not show the progress
        bar after clicking reveal, but somehow the tag is still there,
        even though I cannot see it.

        ! WARN: 
        Some (many) questions do not have a most voted answer as the
        correct answer is actually the one selected by ExamTopics.
        As such, to mitigate the issue, we use the fact that every Card
        has tag <p class="card-text question-answer bg-light white-text">.
        If it doesn't have "vote-bar progress-bar bg-primary", we'll
        default to the primary answer.
        """

        cabody = soup.find_all("div", attrs={'class': "progress vote-distribution-bar"})  # correct answers body

        canswers = []
        for body in cabody:
            # ================ HERE ===============
            # Modify so it defaults to the answer chosen by ExamTopics to mitigate bug on page 10
            card_cans = body.find_all("p", attrs={'class': "card-text question-answer bg-light white-text"}) # !!!
            cans = card_cans.find("div", attrs={'class': "vote-bar progress-bar bg-primary"}).text  # corect answer on a card
            cans = cans.split(" ")[0]  # answer is usually of type "<letter> <percentage>" and we only want the letter
            canswers.append(cans)
            # ======================================

        return canswers


    def get_questions(self) -> list:
        """ Momentarily for debugging purposes I suppose.

            Returns all questions (?)
        """

        questions = []
        for page in self.pages_list:
            questions.append(page.questions)
        return questions 


if __name__ == "__main__":
    quiz = Quiz()