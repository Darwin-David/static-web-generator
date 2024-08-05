# src/nodes/parentnode.py
from .htmlnode import HTMLNode  # Use relative import

class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        if not tag:
            raise ValueError("Tag must be provided")
        if not children:
            raise ValueError("Children must be provided")
        self.tag = tag
        self.children = children

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is required")
        if not self.children:
            raise ValueError("Children nodes required")
        html = f"<{self.tag}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html
