import unittest
from src.split_nodes import split_nodes_image, split_nodes_link
from src.text_node import TextNode

class TestSplitNodes(unittest.TestCase):

    def setUp(self):
        # Common setup for your tests, if needed.
        pass

    # Test cases for split_nodes_image
    def test_split_nodes_image_single(self):
        node = TextNode(
            "This is an image ![image alt text](https://www.example.com/image.jpg) and more text",
            'text'
        )
        new_nodes = split_nodes_image([node])
        expected_nodes = [
            TextNode("This is an image ", 'text'),
            TextNode("image alt text", 'image', "https://www.example.com/image.jpg"),
            TextNode(" and more text", 'text')
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_image_multiple(self):
        node = TextNode(
            "This is an image ![alt1](https://example.com/1.jpg) and another ![alt2](https://example.com/2.jpg)",
            'text'
        )
        new_nodes = split_nodes_image([node])
        expected_nodes = [
            TextNode("This is an image ", 'text'),
            TextNode("alt1", 'image', "https://example.com/1.jpg"),
            TextNode(" and another ", 'text'),
            TextNode("alt2", 'image', "https://example.com/2.jpg")
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_image_none(self):
        node = TextNode(
            "This is a text with no images",
            'text'
        )
        new_nodes = split_nodes_image([node])
        expected_nodes = [node]
        self.assertEqual(new_nodes, expected_nodes)

    # Test cases for split_nodes_link
    def test_split_nodes_link_single(self):
        node = TextNode(
            "This is a link [Boot.dev](https://www.boot.dev) and more text",
            'text'
        )
        new_nodes = split_nodes_link([node])
        expected_nodes = [
            TextNode("This is a link ", 'text'),
            TextNode("Boot.dev", 'link', "https://www.boot.dev"),
            TextNode(" and more text", 'text')
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_link_multiple(self):
        node = TextNode(
            "This is a link [Link1](https://example.com/1) and [Link2](https://example.com/2)",
            'text'
        )
        new_nodes = split_nodes_link([node])
        expected_nodes = [
            TextNode("This is a link ", 'text'),
            TextNode("Link1", 'link', "https://example.com/1"),
            TextNode(" and ", 'text'),
            TextNode("Link2", 'link', "https://example.com/2")
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_link_none(self):
        node = TextNode(
            "This is a text with no links",
            'text'
        )
        new_nodes = split_nodes_link([node])
        expected_nodes = [node]
        self.assertEqual(new_nodes, expected_nodes)

if __name__ == '__main__':
    unittest.main()
