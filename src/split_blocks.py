

def markdown_to_blocks(markdown):
    # step1: split the input string into lines
    lines = markdown.split("\n")

    # Initialize variables to hold blocks and the current block
    blocks = []
    current_block = []

    # Step 2: Detect and gather blocks
    for line in lines:
        if line.strip():  # If the line is not blank
            current_block.append(line)
        else:  # If the line is blank
            if current_block:  # If we have accumulated lines for a block
                blocks.append(' '.join(current_block).strip())
                current_block = []

    
    # Add the last block if there's any
    if current_block:
        blocks.append(' '.join(current_block).strip())

    return blocks
# # Test with an example string to see what it looks like
# test_markdown = """This is **bolded** paragraph

# This is another paragraph with *italic* text and `code` here
# This is the same paragraph on a new line

# * This is a list
# * with items"""

# # Call the function and print the result
# print(markdown_to_blocks(test_markdown))