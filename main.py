import imp


import selenium
import os 

RES_DIR = "./res"  # directory of resources

def get_list_of_html():
    """ Iterates through directory where HTML files are """
    html = []
    for file in os.listdir(RES_DIR):
        _ = os.path.join(RES_DIR, file)
        if os.path.isfile(_):
            html.append(_)
    return html

if __name__ == "__main__":
    html_list = get_list_of_html()
