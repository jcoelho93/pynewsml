import unittest
from unittest import TestCase
from pynewsml import NewsML


class TestNewsML(TestCase):
    def test_newsml(self):
        with open('tests/fixtures/50812345.xml') as fp:
            content = fp.read()
        newsml = NewsML.from_xml(content)

        self.assertEqual(len(newsml.news_items), 1)
        news_item = newsml.news_items[0]
        self.assertEqual(news_item.identifier.provider_id, "AFP")
        self.assertEqual(news_item.identifier.date_id, "20210701")
        self.assertEqual(news_item.identifier.news_item_id, "50812345")
        self.assertEqual(news_item.identifier.revision_id.value, "1")
        self.assertEqual(news_item.identifier.revision_id.update, "N")
        self.assertEqual(
            news_item.identifier.revision_id.previous_revision, "0")
        self.assertEqual(news_item.identifier.public_identifier,
                         "urn:newsml:afp.com:20210701:50812345")


if __name__ == '__main__':
    unittest.main()
