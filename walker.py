from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup
from utils import HTMLFilter
from document_distance import word_vector, page_similarity
from wikipage import WikiPage

class NoPageException(Exception):
    pass
class WikiWalker():
    base_url = "https://en.wikipedia.org/w/api.php"

    @property
    def session(self):
        return requests.Session()

    def parse_page(self, page):
        params = {
            "action": "parse",
            "page": f"{page}",
            "format": "json"
        }
        try:
            soup = BeautifulSoup(self.session.get(self.base_url,params=params).json()['parse']['text']['*'])
            links = link_parser(soup.find_all('a', href=True), filtered_out_terms=['category','special','#', 'ISBN'],required_terms=['wiki'])
            text = soup.text
            wv = word_vector(text)

            return WikiPage(text=text,links=links,title=page, word_vector=wv)
        except KeyError:
            raise NoPageException

def link_parser(list_of_soups, filtered_out_terms, required_terms):
    """


    :param list_of_soups:
    :return :
    """
    response = []
    for soup in list_of_soups:
        if any([soup.attrs['href'].lower().__contains__(a) for a in filtered_out_terms]) or any([not soup.attrs['href'].lower().__contains__(b) for b in required_terms]):
            continue
        if soup.text == '':
            continue
        response.append({'name':soup.text,'href':soup.attrs['href']})
    return response