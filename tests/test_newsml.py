import unittest
from unittest import TestCase
from pynewsml import NewsML


class TestNewsML(TestCase):
    def test_newsml(self):
        with open('tests/fixtures/50812345.xml') as fp:
            content = fp.read()
        newsml = NewsML.from_xml(content)

        self.assertEqual(len(newsml.news_items), 1)

        item = newsml.news_items[0]

        self.assertEqual(
            item.news_component.descriptive_metadata.location.city,
            "Lisboa"
        )
        self.assertEqual(
            item.news_component.descriptive_metadata.location.country_name,
            "Portugal"
        )
        self.assertEqual(item.news_lines.byline, "Maria Antunes")


if __name__ == '__main__':
    unittest.main()
