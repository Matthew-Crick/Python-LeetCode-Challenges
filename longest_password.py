import unittest


class LongestPassword:
    """ LongestPassword class creates a class object whose solve method
    determines the longest valid password against the three following format restrions:
        it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
        there should be an even number of letters;
        there should be an odd number of digits.

    Assume that:

        N is an integer within the range [1..200];
        string S consists only of printable ASCII characters and spaces.
        if there are K spaces in string S then there are exactly K + 1 words.
    """

    def __init__(self) -> None:
        """ initialises the count """
        self.count = -1

    def solve(self, word):
        """ determines the length of the longest valid password from the
        non-empty string word consisting of N characters
        :input: word: a non-empty string with possible spaces
        :output: integer reflecting the length of longest valid password
        :pre-condition: word is non-empty
        :post-condition: output if any is a subset of input
        :time-complexity: O(N)
        :aux-space-complexity: O(1)      
        """
        if word is None or "":
            return -1
        else:
            #  split string by spaces
            words = word.split(" ")

            #  for all seperated words
            for query in words:

                #  if word contains only alphanumeric
                if query.isalnum():

                    #  set respective letter and digit count
                    lc, dc = 0, 0

                        #  then for every character in valid word
                    for char in query:

                        #  if letter; increment letter count
                        if char.isalpha():
                            lc += 1
                        else:

                        #  otherwise increment numeric count
                            dc += 1

                #  valid password if even letter count and odd digit count
                if lc % 2 == 0 and dc % 2 == 1:

                    #  update if new best length
                    if len(query) > self.count:
                        self.count = len(query)
            
            return self.count


class MyTestCase(unittest.TestCase):


    def test_1(self):
        self.assertEqual((LongestPassword().solve("test 5 a0A pass007 ?xy1")), 7)


if __name__ == '__main__':
    unittest.main()
