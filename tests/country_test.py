import unittest

from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country = Country("Germany")

    def test_country_has_name(self):
        self.assertEqual("Germany", self.country.name)

    def test_country_has_id(self):
        self.assertEqual(None, self.country.id)