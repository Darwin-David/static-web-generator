import unittest
from src.nodes import TextNode
from src.parser import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    # Constant setup to use in tests
    text_type_text = "text"
    text_type_code = "code"

    def test_single_delimiter(self):
        node = TextNode("This is text with a `code block` word", self.text_type_text)
        expected = [
            TextNode("This is text with a ", self.text_type_text),
            TextNode("code block", self.text_type_code),
            TextNode(" word", self.text_type_text),
        ]
        result = split_nodes_delimiter([node], "`", self.text_type_code)
        self.assertEqual(result, expected)
    
    def test_no_delimiter(self):
        node = TextNode("This is just plain text", self.text_type_text)
        expected = [TextNode("This is just plain text", self.text_type_text)]
        result = split_nodes_delimiter([node], "`", self.text_type_code)
        self.assertEqual(result, expected)
    
    def test_multiple_delimiters(self):
        node = TextNode("Text with `code` and more `code` blocks", self.text_type_text)
        expected = [
            TextNode("Text with ", self.text_type_text),
            TextNode("code", self.text_type_code),
            TextNode(" and more ", self.text_type_text),
            TextNode("code", self.text_type_code),
            TextNode(" blocks", self.text_type_text),
        ]
        result = split_nodes_delimiter([node], "`", self.text_type_code)
        self.assertEqual(result, expected)
    
    def test_unmatched_delimiter(self):
        node = TextNode("Text with `unmatched delimiter", self.text_type_text)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", self.text_type_code)
        
        self.assertTrue("Unmatched delimiter" in str(context.exception))

    def test_non_text_node(self):
        node
