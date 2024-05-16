import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_url_none(self):
        node = TextNode("This is a text node", "bold", url=None)
        node2 = TextNode("This is a text node", "bold", url=None)
        self.assertEqual(node, node2)
    
    def test_different_type(self):
        node1 = TextNode("Text node", "bold")
        node2 = TextNode("Text node", "italic")
        self.assertNotEqual(node1, node2)
    
    def test_different_text(self):
        node1 = TextNode("Text node1", "bold")
        node2 = TextNode("Text node2", "bold")
        self.assertNotEqual(node1, node2)
    


if __name__ == "__main__":
    unittest.main()