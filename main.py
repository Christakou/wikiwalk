from walker import WikiWalker, NoPageException
from wikipage import WikiPage
from document_distance import page_similarity
import random

IMPROVEMENT_FACTOR = 0.98
def find_path(source, destination):
    path = []
    walker = WikiWalker()
    wiki_page_starting = walker.parse_page(source)
    current_page = wiki_page_starting
    wiki_page_destination = walker.parse_page(destination)
    path.append(wiki_page_starting.title)
    current_similarity = page_similarity(wiki_page_starting,wiki_page_destination)
    print(f'Initial similarity between f{wiki_page_starting} and {wiki_page_destination} is {current_similarity}')
    while current_page != wiki_page_destination:
        for link in current_page.links:

            try:
                temp_page = walker.parse_page(link['name'])

            except NoPageException:
                continue
            temp_page_similarity = page_similarity(temp_page,wiki_page_destination)
            print(f'{current_page} -> {temp_page} -> {wiki_page_destination}')
            print(f' current_similarity: {current_similarity} temp_similarity: {temp_page_similarity}')
            if current_similarity * IMPROVEMENT_FACTOR > temp_page_similarity:
                current_page = temp_page
                current_similarity = temp_page_similarity
                path.append(temp_page.title)
                print('a new step has been taken:')
                print(f'current path:   {path}')

if __name__=='__main__':
    find_path('Lycanthrope','Alien')
