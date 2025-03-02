from unittest import TestCase
from pynewsml import NewsML


class TestNewsML(TestCase):
    def setUp(self):
        with open('tests/fixtures/50812345.xml', encoding='iso-8859-1') as fp:
            self.content = fp.read()
        self.newsml = NewsML.from_xml(self.content)

    def test_newsml_parsing(self):
        self.assertEqual(len(self.newsml.news_items), 1)

    def test_location_parsing(self):
        item = self.newsml.news_items[0]
        self.assertEqual(
            item.news_component.descriptive_metadata.location.city,
            "Lisboa"
        )
        self.assertEqual(
            item.news_component.descriptive_metadata.location.country_name,
            "Portugal"
        )

    def test_author_parsing(self):
        item = self.newsml.news_items[0]
        self.assertEqual(item.news_lines.byline, "Maria Antunes")

    def test_content_parsing(self):
        item = self.newsml.news_items[0]
        self.assertEqual(len(item.content), 2)
        for content in item.content:
            if content.data_content == 'Photo':
                self.assertIsNotNone(content.href)
            if content.data_content == 'HTML':
                self.assertIsNotNone(content.data_content)

    def test_date_parsing(self):
        item = self.newsml.news_items[0]

        self.assertEqual(item.date_label.year, 2025)
        self.assertEqual(item.date_label.month, 1)
        self.assertEqual(item.date_label.day, 28)
        self.assertEqual(item.date_label.hour, 10)
        self.assertEqual(item.date_label.minute, 15)
        self.assertEqual(item.date_label.second, 30)

        self.assertEqual(item.identifier.date_id, "20250128")
