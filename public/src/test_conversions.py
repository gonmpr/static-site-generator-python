import unittest
from conversions import *
from textnode import TextNode, TextType


node = TextNode("**This is text** with a **code block** word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "**", TextType.CODE)
print(new_nodes)
