from htmlnode import HTMLNode
from split_blocks import markdown_to_blocks

def convert_header(block):
    # Determine the level of the header from the number of '#' characters
    level = block.count("#")
    # Extract the header text by removing the '#' characters
    header_text = block.strip("#").strip()
    # Create an HTMLNode with the correct header level
    html_node = HTMLNode(tag=f"h{level}", children=[header_text])
    return html_node


def convert_paragraph(block):
    # Strip any leading/trailing whitespace
    text = block.strip()
    # Create and HTMLNode for a paragraph
    html_node = HTMLNode(tag='p', children=[text])
    return html_node


def convert_unordered_list(block):
    items = block.split('\n')
    li_nodes = [HTMLNode(tag='li', children=[items.strip('*').strip()]) for item in items]
    html_node = HTMLNode(tag='ul', children=li_nodes)
    return html_node


def convert_ordered_list(block):
    items = block.split('\n')
    li_nodes = [HTMLNode(tag='li', children=[item.strip('1. ').strip()]) for item in items]
    html_node = HTMLNode(tag='ol', children=li_nodes)
    return html_node


def convert_blockquote(block):
    text = block.strip('>').strip()
    html_node = HTMLNode(tag='blockquote', children=[text])
    return html_node


def convert_code_block(block):
    code_text = block.strip('`').strip()
    code_node = HTMLNode(tag='code', children=[code_text])
    pre_node = HTMLNode(tag='pre', children=[code_node])
    return pre_node



def markdown_to_html_node(markdown):
    # Split the markdown into blocks (assuming you have a function to do this)
    blocks = markdown_to_blocks(markdown)

    # Determine type and convert each block
    html_nodes = []
    for block in blocks:
        if block.startswith('#'):
            html_nodes.append(convert_header(block))
        elif block.startswith('>'):
            html_nodes.append(convert_blockquote(block))
        elif block.startswith('*'):
            html_nodes.append(convert_unordered_list(block))
        elif block[0].isdigit() and block[1] == '.':
            html_nodes.append(convert_ordered_list(block))
        elif block.startswith('```'):
            html_nodes.append(convert_code_block(block.strip('```')))
        else:
            html_nodes.append(convert_paragraph(block))
    
    # Create a top-level <div> node to hold all the blocks
    top_node = HTMLNode(tag='div', children=html_nodes)
    return top_node




