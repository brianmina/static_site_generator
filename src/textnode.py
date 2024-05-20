
from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        if not isinstance(other, TextNode):
            return False
        
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self) -> str:
        return f" TextNode({self.text}, {self.text_type}, {self.url})"
            

# # Example usage 
# node1 = TextNode("Hello", "bold", "https://example.com")
# node2 = TextNode("Hello", "bold", "https://example.com")
# node3 = TextNode("Hello", "italic", "https://example.com")

# print(node1 == node2) # Expected output: True, as all properties match
# print(node1 == node3) # Expected output: False, as 'text_type' differs
# print(node1 == "Some string") # Expected output: False, as the types differ


# # Example usage
# node = TextNode("Hello", "bold", "https://example.com")
# print(repr(node))  # Output: TextNode(Hello, bold, https://example.com)


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
