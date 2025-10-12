import unittest

from textnode import TextNode, TextType

if __name__ == "__main__":
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

        def test_repr(self):
            node = TextNode("Hello", TextType.PLAIN, "http://example.com")
            expected = "TextNode('Hello', TextType.PLAIN, 'http://example.com')"
            self.assertEqual(repr(node), expected)

        def test_eq_with_different_url(self):
            node1 = TextNode("Text", TextType.LINK, "http://a.com")
            node2 = TextNode("Text", TextType.LINK, "http://b.com")
            self.assertNotEqual(node1, node2)

        def test_eq_with_non_textnode(self):
            node = TextNode("Text", TextType.PLAIN)
            self.assertNotEqual(node, "Text")

        def test_all_text_types(self):
            for text_type in TextType:
                node = TextNode("Sample", text_type)
                self.assertEqual(node.text_type, text_type)

        def test_empty_text(self):
            node = TextNode("", TextType.PLAIN)
            self.assertEqual(node.text, "")

        def test_url_is_optional(self):
            node = TextNode("Text", TextType.IMAGE)
            self.assertIsNone(node.url)
            node2 = TextNode("Text", TextType.IMAGE, "http://img.com")
            self.assertEqual(node2.url, "http://img.com")


    if __name__ == "__main__":
        unittest.main()