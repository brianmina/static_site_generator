
import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


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
        



class TestLeafNode(unittest.TestCase):
     def test_html_node_basics(self):
        node = LeafNode("div", "Hola", {"id": "main", "class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hola")
        #pending to test props in the future


class TestParentNode(unittest.TestCase):

    def setUp(self):
        self.leaf1 = LeafNode("b", "Bold text")
        self.leaf2 = LeafNode(None, "Normal text")
        self.leaf3 = LeafNode("i", "Italic text")

    def test_valid_initialization(self):
        node = ParentNode("div", [self.leaf1, self.leaf2])
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children, [self.leaf1, self.leaf2])
    
    def test_to_html(self):
        # Test to_html method
        node = ParentNode("p", [self.leaf1, self.leaf2, self.leaf3])
        expected_html = "<p><b>Bold text</b>Normal text<i>Italic text</i></p>"
        self.assertEqual(node.to_html(), expected_html)
    
    def test_nested_parent_nodes(self):
        # Test nested ParentNode
        child_node = ParentNode("span", [self.leaf1])
        parent_node = ParentNode("div", [child_node, self.leaf2])
        expected_html = "<div><span><b>Bold text</b></span>Normal text</div>"
        self.assertEqual(parent_node.to_html(), expected_html)
    
   
        



if __name__ == "__main__":
    unittest.main()