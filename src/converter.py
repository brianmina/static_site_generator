from textnode import TextNode
from htmlnode import LeafNode


def text_node_to_html_node(text_node):
    if text_node.type == "text":
        return LeafNode(tag=None, text=text_node.text)
    
    elif text_node.type == "bold":
        return LeafNode(tag="b", text=text_node.text)
    
    elif text_node.type == "italic":
        return LeafNode(tag="i", text=text_node.text)
    
    elif text_node.type == "code":
        return LeafNode(tag="code", text=text_node.text)
    
    elif text_node.type == "link":
        return LeafNode(tag="a", text=text_node.text, props={"href": text_node.href})
    
    elif text_node.type == "image":
        return LeafNode(tag="img", text="", props={"src": text_node.src, "alt": text_node.alt})
    
    else:
        raise Exception("Unsupported TextNode type")



