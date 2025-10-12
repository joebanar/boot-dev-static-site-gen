import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_notEq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_urlNone(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertIsNone(node.url)

    def test_urlProvided(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.google.com")
        self.assertIsNotNone(node.url)


if __name__ == "__main__":
    unittest.main()