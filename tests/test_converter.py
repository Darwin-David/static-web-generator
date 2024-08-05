import unittest
from src.textnode import TextNode
from src.htmlnode import LeafNode
from src.converter import text_node_to_html_node

class TestTextNodeToHtmlNode(unittest.TestCase):

    def test_text_node(self):
        node = TextNode(TextNode.TEXT, "some text")
        result = text_node_to_html_node(node)
        expected = LeafNode('', 'some text')
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.text, expected.text)
        self.assertEqual(result.attrs, expected.attrs)

    def test_bold_node(self):
        node = TextNode(TextNode.BOLD, "bold text")
        result = text_node_to_html_node(node)
        expected = LeafNode('b', 'bold text')
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.text, expected.text)
        self.assertEqual(result.attrs, expected.attrs)

    def test_italic_node(self):
        node = TextNode(TextNode.ITALIC, "italic text")
        result = text_node_to_html_node(node)
        expected = LeafNode('i', 'italic text')
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.text, expected.text)
        self.assertEqual(result.attrs, expected.attrs)

    def test_code_node(self):
        node = TextNode(TextNode.CODE, "code text")
        result = text_node_to_html_node(node)
        expected = LeafNode('code', 'code text')
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.text, expected.text)
        self.assertEqual(result.attrs, expected.attrs)

    def test_link_node(self):
        node = TextNode(TextNode.LINK, "link text", href="http://example.com")
        result = text_node_to_html_node(node)
        expected = LeafNode('a', 'link text', href="http://example.com")
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.text, expected.text)
        self.assertEqual(result.attrs, expected.attrs)

    def test_image_node(self):
        node = TextNode(TextNode.IMAGE, "", src="http://example.com/image.jpg", alt="example image")
        result = text_node_to_html_node(node)
        expected = LeafNode('img', '', src="http
