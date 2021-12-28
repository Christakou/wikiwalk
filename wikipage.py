from dataclasses import dataclass


@dataclass
class WikiPage():
    title: str
    text: str
    links: list
    word_vector: dict
    def __str__(self):
        return f'{self.title}'

    def __eq__(self, other):
        if self.text == other.text:
            return True
        else:
            return False
