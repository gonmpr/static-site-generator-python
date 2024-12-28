import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        html_node = HTMLNode('<h1>', 'this is a title')
        print(html_node)

    def test_edge(self):
        html_node = HTMLNode('<a>', 'this is a tag',props={"href": "https://www.google.com"})
        print(html_node)
        print(html_node.props_to_html())

    def test_edge2(self):
        html_node = HTMLNode('<p>', 'this is a paragraph with no props')
        print(html_node)
        print(html_node.props_to_html())


if __name__ == "__main__":
    unittest.main()
