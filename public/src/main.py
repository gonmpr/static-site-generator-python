from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from conversions import *

def main():

    text_node = LeafNode('b', 'ayayaya', props={'url':'home/gonmpr'})


    print(text_node.to_html())


























if __name__ == '__main__':
    main()
