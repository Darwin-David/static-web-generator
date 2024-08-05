import unittest
from main import extract_markdown_images, extract_markdown_links

class TestMarkdownExtractors(unittest.TestCase):

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_output = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), expected_output)

        text_empty = "This text has no images!"
        expected_empty = []
        self.assertEqual(extract_markdown_images(text_empty), expected_empty)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected_output = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text), expected_output)

        text_empty = "This text has no links!"
        expected_empty = []
        self.assertEqual(extract_markdown_links(text_empty), expected_empty)


if __name__ == '__main__':
    unittest.main()
