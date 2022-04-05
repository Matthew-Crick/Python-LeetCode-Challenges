import unittest


def solution(p: int, c: int):
    """ given the number of players P and the number of reserved courts C,
    returns the maximum number of 1v1 games that can be played in parallel.
    :param p: integer reflecting the number of players
    :param c: integer reflecting the number of courts
    :return: integer reflecting the maximum number of 1v1 games that can be played
    """
    if c == 0 or p == 0 or p == 1:

        #  insufficient input
        return 0
    else:

        #  matches
        match_ups = p // 2

        #  if enough courts
        if c >= match_ups:

            #  as many matches
            return match_ups

        #  if limited courts
        elif match_ups >= c:

            #  as many courts
            return c


class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution(5, 3), 2)

    def test_2(self):
        self.assertEqual(solution(10, 3), 3)

    def test_3(self):
        self.assertEqual(solution(20, 10), 10)

    def test_4(self):
        self.assertEqual(solution(2, 10), 1)

    def test_5(self):
        self.assertEqual(solution(1, 0), 0)


if __name__ == '__main__':
    unittest.main()
