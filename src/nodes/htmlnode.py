class HTMLNode:
    pass

class LeafNode(HTMLNode):
    def __init__(self, tag, text='', **attrs):
        self.tag = tag
        self.text = text
        self.attrs = attrs

    def __repr__(self):
        return f"LeafNode(tag='{self.tag}', text='{self.text}', attrs={self.attrs})"
