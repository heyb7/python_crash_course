import unittest
from city_functions import  city_country

class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")

    def test_city_country_population(self):
        result = city_country("santiago", "chile", 5000000)
        self.assertEqual(result, "Santiago, Chile - Population 5000000")
unittest.main()