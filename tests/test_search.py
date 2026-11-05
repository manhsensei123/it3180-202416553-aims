import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class TestSearch(unittest.TestCase):
    def test_search_by_category(self):
        items = [
            DigitalVideoDisc("The Lion King", category="Animation"),
            DigitalVideoDisc("Star Wars", category="Sci-Fi"),
        ]
        self.assertEqual(len(search_by_category(items, "animation")), 1)

    def test_search_by_title_match(self):
        items = [DigitalVideoDisc("The Lion King"), DigitalVideoDisc("Star Wars")]
        result = search_by_title(items, "Star")
        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()
