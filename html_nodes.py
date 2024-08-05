class HTMLNode:
    def __init__(self, tag, attributes={}):
        self.tag = tag
        self.attributes = attributes
        self.children = []

    def to_html(self):
        # An example method for HTMLNode, to be overridden in LeafNode
        pass

class LeafNode(HTMLNode):
    def __init__(self, tag, value, attributes={}):
        super().__init__(tag, attributes)
        self.children = []
        if value is None:
            raise ValueError("LeafNode must have a value")
        self.value = value

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        attributes_str = " ".join([f'{key}="{val}"' for key, val in self.attributes.items()])
        if attributes_str:
            return f"<{self.tag} {attributes_str}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
