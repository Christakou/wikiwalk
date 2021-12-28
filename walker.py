from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup
from utils import HTMLFilter

@dataclass
class WikiPage():
    title: str
    text: str
    links: list

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

        data = self.session.get(self.base_url, params=params).json()
        soup = BeautifulSoup(self.session.get(self.base_url,params=params).json()['parse']['text']['*'])
        links = link_parser(soup.find_all('a', href=True), filtered_terms=['category'])
        text = soup.text
        word_vector =

        return WikiPage(text=text,links=links,title=page)

def link_parser(list_of_soups, filtered_terms):
    """


    :param list_of_soups:
    :return :
    """
    response = []
    for soup in list_of_soups:
        if any([soup.attrs['href'].lower().__contains__(a) for a in filtered_terms]):
            continue
        response.append({soup.attrs['href']:soup.text})
    return response

a = WikiWalker()
a.read_page('werewolf')