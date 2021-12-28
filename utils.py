from html.parser import HTMLParser

class HTMLFilter(HTMLParser):
    text = ""
    def handle_data(self, data):
        self.text += data


