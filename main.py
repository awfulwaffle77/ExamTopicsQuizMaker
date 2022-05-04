from bs4 import BeautifulSoup as bs
import os 

RES_DIR = "./res"  # directory of resources

def get_list_of_html() -> list:
    """ Iterates through directory where HTML files are and
        returns their names
    """
    html = []
    for file in os.listdir(RES_DIR):
        _ = os.path.join(RES_DIR, file)
        if os.path.isfile(_):
            html.append(_)
    return html  # order is irrelevant


def init_soup(html_list: list):
    """ Creates a list of soups so that we can easily parse each of them """
    soup_list = [] 
    print(len(html_list))
    for html_file in html_list:
        with open(html_file, "r", encoding="utf8") as fhandler:
            soup = bs(fhandler.read(), "html.parser")
            soup_list.append(soup)
    return soup_list

def get_question_bodies(soup):
    return soup.find_all("div", attrs={'class': "question-body"})


if __name__ == "__main__":
    soup_list = init_soup(get_list_of_html())
    
    idx = 0
    for s in soup_list:
        idx += 1 
        print("=" * 20, idx, "=" * 20)
        print(get_question_bodies(s))
        if idx == 1:
            break
    # print(len(soup_list))