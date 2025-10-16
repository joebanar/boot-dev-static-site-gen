import unittest
from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_basic(self):
        md = "# Hello World\nSome content."
        self.assertEqual(extract_title(md), "Hello World")

    def test_extract_title_with_spaces(self):
        md = "   #   Title With Spaces   \nOther text"
        self.assertEqual(extract_title(md), "Title With Spaces")

    def test_extract_title_multiple_headers(self):
        md = "# First Title\n## Subtitle\n# Second Title"
        self.assertEqual(extract_title(md), "First Title")

    def test_extract_title_no_h1(self):
        md = "## Subtitle\nSome text"
        with self.assertRaises(Exception):
            extract_title(md)

    def test_extract_title_h1_not_first_line(self):
        md = "Some intro\n# Actual Title\nMore text"
        self.assertEqual(extract_title(md), "Actual Title")

    def test_extract_title_empty_string(self):
        md = ""
        with self.assertRaises(Exception):
            extract_title(md)

    def test_extract_title_h1_with_special_chars(self):
        md = "# Title! @2024\nContent"
        self.assertEqual(extract_title(md), "Title! @2024")

if __name__ == "__main__":
    unittest.main()
