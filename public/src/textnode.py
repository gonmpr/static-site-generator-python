'''
This is a intermediate representation of the text in the
markdown -> HTML conversion
for the inline elements
'''

from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if [self.text, self.text_type, self.url] == [other.text,other.text_type,other.url]:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text},{self.text_type},{self.url})"





























