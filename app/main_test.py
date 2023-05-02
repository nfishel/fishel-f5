from main import return_backwards_string, get_mode
import unittest
import os


class TestMain(unittest.TestCase):
    def test_return_backwards_string(self):
        random_string = "This is my test string"
        random_string_reversed = "gnirts tset ym si sihT"
        self.assertEqual(return_backwards_string('hello'), 'olleh')
        self.assertEqual(return_backwards_string('hello world'), 'dlrow olleh')
        self.assertEqual(return_backwards_string('1234567890'), '0987654321')
        self.assertEqual(random_string_reversed,
                         return_backwards_string(random_string))

    def test_get_mode(self):
        self.assertEqual(get_mode(), os.environ.get('MODE'))


if __name__ == '__main__':
    unittest.main()
