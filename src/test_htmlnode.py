import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_leafnode_init_defaults(self):
        node = LeafNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.props)
        self.assertIsNone(node.children)

    def test_leafnode_init_with_values(self):
        node = LeafNode(tag="span", value="Hello", props={"class": "highlight"})
        self.assertEqual(node.tag, "span")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.props, {"class": "highlight"})
        self.assertIsNone(node.children)

    def test_leafnode_value_type_error(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="span", value=123)

    def test_leafnode_to_html_with_tag_and_value(self):
        node = LeafNode(tag="b", value="Bold", props={"style": "font-weight:bold"})
        self.assertEqual(node.to_html(), '<b style="font-weight:bold">Bold</b>')

    def test_leafnode_to_html_with_tag_and_no_props(self):
        node = LeafNode(tag="i", value="Italic")
        self.assertEqual(node.to_html(), '<i>Italic</i>')

    def test_leafnode_to_html_with_no_tag(self):
        node = LeafNode(value="Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leafnode_to_html_with_none_value(self):
        node = LeafNode(tag="p")
        self.assertIsNone(node.to_html())

    def test_leafnode_repr(self):
        node = LeafNode(tag="a", value="Link", props={"href": "https://example.com"})
        expected = "LeafNode(tag='a', value='Link', props={'href': 'https://example.com'})"
        self.assertEqual(repr(node), expected)

    def test_leafnode_props_to_html(self):
        node = LeafNode(tag="img", value="", props={"src": "img.png", "alt": "image"})
        result = node.props_to_html()
        self.assertIn('src="img.png"', result)
        self.assertIn('alt="image"', result)

    def test_init_with_values(self):
        node = HTMLNode(tag="p", value="Hello", children=[], props={"class": "text"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "text"})

    def test_props_to_html_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty_dict(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode(props={"id": "main"})
        self.assertEqual(node.props_to_html(), ' id="main"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={"id": "main", "class": "container"})
        result = node.props_to_html()
        self.assertTrue(
            result == ' id="main" class="container"' or
            result == ' class="container" id="main"'
        )

    def test_repr(self):
        node = HTMLNode(tag="div", value="content", children=[HTMLNode(value="child")], props={"style": "color:red"})
        expected = (
            "HTMLNode(tag='div', value='content', "
            "children=[HTMLNode(tag=None, value='child', children=None, props=None)], "
            "props={'style': 'color:red'})"
        )
        self.assertEqual(repr(node), expected)

    def test_to_html_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    # Additional tests
    def test_props_to_html_special_chars(self):
        node = HTMLNode(props={"data-info": "a&b", "title": 'He said "hi"'})
        result = node.props_to_html()
        self.assertIn('data-info="a&b"', result)
        self.assertIn('title="He said \"hi\""', result)

    def test_repr_none_values(self):
        node = HTMLNode()
        expected = "HTMLNode(tag=None, value=None, children=None, props=None)"
        self.assertEqual(repr(node), expected)

    def test_repr_with_multiple_children(self):
        child1 = HTMLNode(tag="span", value="child1")
        child2 = HTMLNode(tag="span", value="child2")
        node = HTMLNode(tag="div", children=[child1, child2])
        expected = (
            "HTMLNode(tag='div', value=None, "
            "children=[HTMLNode(tag='span', value='child1', children=None, props=None), "
            "HTMLNode(tag='span', value='child2', children=None, props=None)], "
            "props=None)"
        )
        self.assertEqual(repr(node), expected)

    def test_props_to_html_with_int_and_bool(self):
        node = HTMLNode(props={"tabindex": 1, "hidden": True})
        result = node.props_to_html()
        self.assertIn('tabindex="1"', result)
        self.assertIn('hidden="True"', result)

if __name__ == "__main__":
    unittest.main()