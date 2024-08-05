class TextNode:
    def __init__(self, text, type):
        self.text = text
        self.type = type

    def __repr__(self):
        return f"TextNode(text='{self.text}', type='{self.type}')"
