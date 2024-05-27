import unittest


from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    split_node_images,
    split_node_links
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node2", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        node2 = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual("TextNode(This is a text node, text, https://www.boot.dev)", repr(node))


class TestSplitNodesImage(unittest.TestCase):

    def test_split_nodes_image_no_images(self):
        node = TextNode("Just some plain text.", text_type_text)
        new_nodes = split_node_images([node])
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].content, "Just some plain text.")
        self.assertEqual(new_nodes[0].text_type, text_type_text)

    def test_split_nodes_image_single_image(self):
        node = TextNode("Text before ![image](url) text after.", text_type_text)
        new_nodes = split_node_images([node])
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].content, "Text before ")
        self.assertEqual(new_nodes[0].text_type, text_type_text)
        self.assertEqual(new_nodes[1].content, "image")
        self.assertEqual(new_nodes[1].text_type, text_type_image)
        self.assertEqual(new_nodes[1].url, "url")
        self.assertEqual(new_nodes[2].content, " text after.")
        self.assertEqual(new_nodes[2].text_type, text_type_text)


if __name__ == "__main__":
    unittest.main()