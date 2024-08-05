import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from nodes.parentnode import ParentNode
from nodes.htmlnode import HTMLNode  # Assuming HTMLNode base class is imported if needed

# Mock LeafNode for testing purposes
class LeafNode(HTMLNode):
    def __init__(self, tag, value):
        self.tag = tag
        self.value = value

    def to_html(self):
        if self.tag:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return self.value

class TestParentNode(unittest.TestCase):
    
    def test_parent_node_tag(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("", [LeafNode("b", "Test")])
        self.assertTrue('Tag must be provided' in str(context.exception))

    def test_parent_node_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("p", [])
        self.assertTrue('Children must be provided' in str(context.exception))

    def test_parent_node_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        expected_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()
