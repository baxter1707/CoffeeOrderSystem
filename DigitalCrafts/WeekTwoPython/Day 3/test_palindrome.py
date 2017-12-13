import unittest
from palindrometest import Palindrome

class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.palin = Palindrome()

    def test_can_check_palinrome_object(self):
        self.assertNotEqual(self.palin,None)


unittest.main()
