import unittest
from unittest import TestCase
from pynewsml import NewsML


class TestNewsML(TestCase):
    def test_newsml(self):
        with open('tests/fixtures/50812345.xml') as fp:
            content = fp.read()
        newsml = NewsML.from_xml(content)

        self.assertEqual(len(newsml.news_items), 1)


if __name__ == '__main__':
    unittest.main()
