from text_node import TextNode

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == 'text':
            # Split and process the node text based on image pattern
            # Example usage: sections = node.text.split(f"![{image_alt}]({image_link})", 1)
            pass  # Implement your logic here
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == 'text':
            # Split and process the node text based on link pattern
            pass  # Implement your logic here
        else:
            new_nodes.append(node)
    return new_nodes
