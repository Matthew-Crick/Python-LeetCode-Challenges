import unittest


class Solution:
    """ class Solution contains a method isValid which, given a
    string s containing parentheses characters only; determines
    if the input string is a valid parentheses.
    """

    def __init__(self):
        self.s = []

    def is_valid(self, s: str) -> bool:
        # Traverse the input string
        for letter in s:
            if letter in ["(", "{", "["]:

                # Push the element in the stack
                self.s.append(letter)
            else:

                # if not opening, then it must be closing
                # So stack cannot be empty at this point.
                # As stack contains corresponding opening
                if not self.s:
                    return False
                current = self.s.pop()
                if current == '(':
                    if letter != ")":
                        return False
                if current == '{':
                    if letter != "}":
                        return False
                if current == '[':
                    if letter != "]":
                        return False

        # Check if Empty
        if self.s:
            return False
        return True


class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Solution().is_valid("()"), True)

    def test_2(self):
        self.assertEqual(Solution().is_valid("()[]{}"), True)

    def test_3(self):
        self.assertEqual(Solution().is_valid("(]"), False)


if __name__ == '__main__':
    unittest.main()
