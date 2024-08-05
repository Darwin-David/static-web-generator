class TextNode:
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

    def __init__(self, type, content, href=None, src=None, alt=None):
        self.type = type
        self.content = content
        self.href = href
        self.src = src
        self.alt = alt

    def __eq__(self, other):
        return (
	    self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'

