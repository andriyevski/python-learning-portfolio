import unittest
from name_function import get_formatted_name


class TestDataInCase(unittest.TestCase):
    """ Check if data can return from function """

    def name_splitter(self, full_name: str):
        """ All name and last name split """
        splitted_data = full_name.split(' ')
        return splitted_data

    def test_name_comeback(self):
        data_respond = get_formatted_name('janis', 'joplin')
        splitted_name = self.name_splitter(data_respond)
        #print(splitted_name[0])
        self.assertIn('Janis', splitted_name[0])

    def test_last_name_comeback(self):
        data_respond = get_formatted_name('janis', 'joplin')
        splitted_last_name = self.name_splitter(data_respond)
        #print(splitted_last_name[1])
        self.assertIn('Joplin', splitted_last_name[1])

    def test_multiple_names(self):
        """ Test on many names of different people! """
        test_cases = [
            ('janis', 'joplin', ['Janis', 'Joplin']),
            ('antonio', 'Banderas', ['Antonio', 'Banderas']),
            ('Luciano', 'romalio', ['Luciano', 'Romalio']),
        ]
        for first, last, expected in test_cases:
            with self.subTest(first=first, last=last):
                full = get_formatted_name(first, last)
                parts = self.name_splitter(full)
                self.assertEqual(parts, expected)


class NamesTestCase(unittest.TestCase):
    """ Test for 'name_function' """

    def test_first_last_name(self):
        """ Name view 'Janis Joplin' work correct ? """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """ If work 'Wolfgan Amadeus Mozart' ? """
        formatted_name = get_formatted_name('Wolfgan','Mozart','Amadeus')
        self.assertEqual(formatted_name, 'Wolfgan Amadeus Mozart')


if __name__ == "__main__":
    unittest.main()
