from block_to_htmlnode import convert_header
from htmlnode import HTMLNode

def test_convert_header():
    # Test case for H1 header
    block = "# Welcome"
    expected_output = HTMLNode(tag='h1', children=['Welcome'])
    assert convert_header(block).__repr__() == expected_output.__repr__(), f"Test 1 Failed: {convert_header(block)}"

    # Test case for H2 header
    block = "## This is a subheader"
    expected_output = HTMLNode(tag='h2', children=['This is a subheader'])
    assert convert_header(block).__repr__() == expected_output.__repr__(), f"Test 2 Failed: {convert_header(block)}"

    # Test case for H3 header
    block = "### Another subheader"
    expected_output = HTMLNode(tag='h3', children=['Another subheader'])
    assert convert_header(block).__repr__() == expected_output.__repr__(), f"Test 3 Failed: {convert_header(block)}"

    print("All tests passed!")


# Run the test function
test_convert_header()