import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for name_function.py"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('john', 'jenkins')
        self.assertEqual(formatted_name, "John Jenkins")

    
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('ayush', 'srivastava', 'kumar')
        self.assertEqual(formatted_name, "Ayush Kumar Srivastava")


unittest.main()