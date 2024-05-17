
import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html_with_attributes(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        expected = ' href="https://example.com" target="_blank"'       
        self.assertEqual(node.props_to_html(), expected)
    
    def test_prop_to_html_without_attributes(self):
        node = HTMLNode()
        expected = ""
        self.assertEqual(node.props_to_html(), expected)
    
    def test_repr(self):
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://example.com"})
        expected = 'HTMLNode(tag=a, value=Click here, children=0, props={\'href\': \'https://example.com\'})'
        self.assertEqual(repr(node), expected)

    def test_repr_with_children(self):
        # Define a child node
        child_node = HTMLNode(tag="span", value="child")
        
        # Define a parent node with the child node included
        parent_node = HTMLNode(tag="div", children=[child_node])
        
        # The expected representation should count the children correctly
        expected = "HTMLNode(tag=div, value=None, children=1, props=None)"
        
        # Print actual repr output for debugging
        actual_repr = repr(parent_node)
        print(f"Actual repr output: {actual_repr}")
        
        # Print expected for comparison
        print(f"Expected repr output: {expected}")
        
        # Assert they are equal
        self.assertEqual(actual_repr, expected)
        
    def test_to_html_raises_not_implemented_error(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()
        

if __name__ == "__main__":
    unittest.main()