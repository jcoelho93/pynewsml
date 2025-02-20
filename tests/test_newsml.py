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

        self.assertEqual(len(item.content), 2)
        for content in item.content:
            if content.data_content == 'Photo':
                self.assertIsNotNone(content.href)
            if content.data_content == 'HTML':
                self.assertIsNotNone(content.data_content)


if __name__ == '__main__':
    unittest.main()
