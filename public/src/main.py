from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode
def main():

    leaf = LeafNode("a", "Click me!",props= {"href": "https://www.google.com"})
    leaf2 = LeafNode("p", "This is a paragraph of text.")
    leaf3 = LeafNode(value = "Hello World!")
    print(leaf.to_html())
    print(leaf2.to_html())
    print(leaf3.to_html())























if __name__ == '__main__':
    main()
