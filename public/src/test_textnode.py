import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_edge(self):
        node = TextNode("This is a text node failure test type",TextType.ITALIC)
        node2 = TextNode("This is a text node failure test type",TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_edge2(self):
        node = TextNode("This is a text node failure test type",TextType.BOLD,'HOMO')
        node2 = TextNode("This is a text node failure test type",TextType.BOLD,'HOMO')
        self.assertEqual(node, node2)

    def test_edge3(self):
        node = TextNode("This is a text node failure test type",TextType.BOLD,None)
        node2 = TextNode("This is a text node failure test type",TextType.BOLD)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()