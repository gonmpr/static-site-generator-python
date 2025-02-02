from textnode import *
from htmlnode import *


#converts TextNode to HTMLNode
def text_node_to_html(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value=text_node.text)

        case TextType.BOLD:
            return LeafNode(tag='b', value=text_node.text)

        case TextType.ITALIC:
            return LeafNode(tag='i', value=text_node.text)

        case TextType.CODE:
            return LeafNode(tag='code', value=text_node.text)

        case TextType.LINK:
            return LeafNode(tag='a', value= text_node.text, props={'href':f'"{text_node.url}"'})

        case TextType.IMAGE:
            return LeafNode(tag='img', value = '', props={'src':f'"{text_node.url}"', 'alt':f'"{text_node.text}"'})

        case _:
            raise Exception('No valid type of text for a text_node object')


#converts a raw markdown file in a text nodes list
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if delimiter not in old_node.text:
            new_nodes.append(old_node)
            continue

        splited_node = old_node.text.split(delimiter)

        for part in splited_node:
            if (splited_node.index(part)+1) % 2 == 0:
                new_nodes.append(TextNode(part, text_type))

            if (splited_node.index(part)+1) % 2 != 0:
                new_nodes.append(TextNode(part, old_node.text_type))

    return new_nodes
