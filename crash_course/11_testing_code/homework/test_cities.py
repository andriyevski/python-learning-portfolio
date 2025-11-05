import unittest
from Citie_Country import city_country

class DataTestCases(unittest.TestCase):
    def test_citiy_country(self):
         """ Test city_country """
         data = city_country('kyiv','ukraine')
         self.assertEqual(data, 'Citie: Kyiv, Country: Ukraine')

if __name__ == "__main__":
    unittest.main()
