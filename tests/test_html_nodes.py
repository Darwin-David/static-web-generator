import unittest
from html_nodes import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_node_creation(self):
        leaf = LeafNode("p", "This is a paragraph.")
        self.assertEqual(leaf.tag, "p")
        self.assertEqual(leaf.value, "This is a paragraph.")
        self.assertEqual(leaf.attributes, {})
        self.assertEqual(leaf.children, [])

    def test_leaf_node_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_leaf_node_to_html(self):
        # Test without attributes
        leaf = LeafNode("p", "This is a paragraph.")
        self.assertEqual(leaf.to_html(), "<p>This is a paragraph.</p>")

        # Test with attributes
        leaf_with_attrs = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf_with_attrs.to_html(), '<a href="https://www.google.com">Click me!</a>')

        # Test with no tag (raw text)
        leaf_no_tag = LeafNode(None, "Just text.")
        self.assertEqual(leaf_no_tag.to_html(), "Just text.")

        # Test raising ValueError if value is not set in to_html
        leaf_no_value = LeafNode("b", "")
        with self.assertRaises(ValueError):
            leaf_no_value.to_html()

if __name__ == "__main__":
    unittest.main()
