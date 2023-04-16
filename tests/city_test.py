import unittest

from repositories import city_repository
from repositories import country_repository
from models.country import Country
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.country_1 = Country("Germany", None)
        self.city_1 = City("Berlin", self.country_1.name, False, None)

    def test_city_has_name(self):
        self.assertEqual("Berlin", self.city_1.name)

    

    

