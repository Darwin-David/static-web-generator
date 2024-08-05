from .textnode import TextNode
from .htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.type == TextNode.TEXT:
        return LeafNode('', text_node.content)
    elif text_node.type == TextNode.BOLD:
        return LeafNode('b', text_node.content)
    elif text_node.type == TextNode.ITALIC
