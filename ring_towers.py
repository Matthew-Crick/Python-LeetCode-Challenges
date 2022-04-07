import unittest


class Solution:
    """Solution class"""

    def __init__(self) -> None:
        """Initialise instance variable containers"""
        self.towers = [[] for _ in range(10)]
        self.letters, self.rods, self.successful = [], [], []

    def count_points(self, rings: str) -> int:
        """ Counts the number of successful rods containing at least 1 of each coloured ring.
        :input: rings: Every two characters in rings forms a colour-position pair where 
        first character is of {'B', 'G', 'R'} and second character is of {'0-9'}.
        :return: Number of rods that contain at least one each colour.
        :pre-condition: Input contains {'B', 'G', 'R', '0-9'} and follows colour-position pair input
        :post-condition: Number of rods returned must be within the range 0-10
        :time-complexity: O(N)
        :aux-space-complexity: O(1)
        """
        #  split coloured rings from rod allocations
        for i in range(len(rings)):
            if i % 2 == 0:
                self.letters.append(rings[i])  # colour
            else:
                self.rods.append(int(rings[i]))  # rod

        #  add coloured ring to respective rod allocation
        for j in range(len(self.letters)):
            self.towers[self.rods[j]].append(self.letters[j])

        #  assess rods for all coloured rings
        for i in range(len(self.towers)):

            #  cannot have all colours if
            if len(self.towers[i]) < 3:
                continue

            #  otherwise, assess for each individual colour
            else:
                if 'B' in self.towers[i]:
                    if 'G' in self.towers[i]:
                        if 'R' in self.towers[i]:
                            #  add successful
                            self.successful.append(i)

        #  numbers of successful rods
        return len(self.successful)


class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Solution().count_points("B0B6G0R6R0R6G9"), 1)

    def test_2(self):
        self.assertEqual(Solution().count_points("B0R0G0R9R0B0G0"), 1)

    def test_3(self):
        self.assertEqual(Solution().count_points("G4"), 0)

    def test_4(self):
        self.assertEqual(Solution().count_points("B2G2R2"), 1)

    def test_5(self):
        self.assertEqual(Solution().count_points("B2G2R2B2G2R2"), 1)

    def test_6(self):
        self.assertEqual(Solution().count_points("B2G2R2B4G4R4"), 2)

    def test_7(self):
        self.assertEqual(Solution().count_points("G6B6B0G1B0G6G7G2G6R9G0G9B1G5"), 0)


if __name__ == '__main__':
    unittest.main()
