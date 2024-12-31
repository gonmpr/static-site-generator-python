from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
def main():

    leaf = LeafNode("a", "Click me!",props= {"href": "https://www.google.com"})
    leaf2 = LeafNode("p", "This is a paragraph of text.")
    leaf3 = LeafNode(value = "Hello World!")

    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

    node2 = ParentNode(
    "i",
    [
        LeafNode("b", "LALALALA"),
        LeafNode(None, "LALALA"),
        node
    ],
)

    print(node2.to_html())
























if __name__ == '__main__':
    main()
