from src.nodes import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.type != "text":
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise Exception(f"Unmatched delimiter `{delimiter}` found in text: '{node.text}'")

        for i in range(len(parts)):
            if i % 2 == 0:
                new_nodes.append(TextNode(parts[i], "text"))
            else:
                new_nodes.append(TextNode(parts[i], text_type))

    return new_nodes
