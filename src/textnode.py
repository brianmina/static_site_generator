from htmlnode import LeafNode
from extract_regex import extract_markdown_images, extract_markdown_links

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")



def split_node_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == text_type_text:
            images = extract_markdown_images(node.content)

            if not images:
                # No images found, append the original node
                new_nodes.append(node)
                continue
            
            # Start with the original text
            curr_text = node.content

            for alt_text, img_url in images:
                # Split around the first image found
                before_img, after_img = curr_text.split(f"![{alt_text}]({img_url})", 1)

                # Append the part before the image if it's not empty
                if before_img:
                    new_nodes.append(TextNode(before_img, text_type_text))
                # Append the image itself as a TextNode
                new_nodes.append(TextNode(alt_text, text_type_image, img_url))

                # Continue processing the remainder of the text
                curr_text =  after_img
            
            # After all images are processed, append any remaining text
            if curr_text:
                new_nodes.append(TextNode(curr_text,text_type_text))

        else:
            # For any non-text type, just append the node as it is
            new_nodes.append(node)
    
    return new_nodes





def split_node_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == text_type_text:
            links = extract_markdown_links(node.content)

            if not links:
                new_nodes.append(node)
                continue
             # Start with the original text
            curr_text = node.content

            for alt_text, link_url in links:
                # Split around the first image found
                before_lnk, after_lnk = curr_text.split(f"![{alt_text}]({link_url})", 1)

                # Append the part before the image if it's not empty
                if before_lnk:
                    new_nodes.append(TextNode(before_lnk, text_type_text))
                # Append the image itself as a TextNode
                new_nodes.append(TextNode(alt_text, text_type_image, link_url))

                # Continue processing the remainder of the text
                curr_text =  after_lnk
            
            # After all images are processed, append any remaining text
            if curr_text:
                new_nodes.append(TextNode(curr_text,text_type_text))

        else:
            # For any non-text type, just append the node as it is
            new_nodes.append(node)
    
    return new_nodes
