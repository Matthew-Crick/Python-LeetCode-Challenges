import unittest


class Solution:
    """ Solution class."""

    def __init__(self):
        """ initialise converted value variable """
        self.val = 0

    def roman_to_int(self, s):
        """ Converts a roman numeral string to its corresponding integer.
        :input: s: a roman numeral string
        :return: integer reflecting the converted roman numeral
        :pre-condition:  s is a valid roman numeral in the range [1, 3999] having ('I', 'V', 'X', 'L', 'C', 'D', 'M').
        :post-condition: integer in the range [1, 3999]
        :time-complexity: O(N)
        :aux-time-complexity: O(1)
        """

        #  dictionary mapping roman numeral to its corresponding integer value
        roman_map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        #  iterate over input
        for i in range(0, len(s) - 1):

            #  if current is less than next; subtract
            if roman_map[s[i]] < roman_map[s[i + 1]]:
                self.val -= roman_map[s[i]]
            else:

                #  otherwise, add
                self.val += roman_map[s[i]]

                #  return count and add last letter
        return self.val + roman_map[s[-1]]


class MyTestCase(unittest.TestCase):
    """ tests"""

    def test_1(self):
        self.assertEqual(Solution().roman_to_int("III"), 3)

    def test_2(self):
        self.assertEqual(Solution().roman_to_int("LVIII"), 58)

    def test_3(self):
        self.assertEqual(Solution().roman_to_int("MCMXCIV"), 1994)


if __name__ == '__main__':
    unittest.main()
