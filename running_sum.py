import unittest


class Solution:

    def __init__(self):
        self.output = None

    def runningSum(self, nums):
        self.output = [0] * len(nums)
        self.output[0] = nums[0]

        for i in range(1, len(nums)):
            self.output[i] += self.output[i-1] + nums[i]
        return self.output


class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Solution().runningSum([1, 2, 3, 4]), [1, 3, 6, 10])

    def test_2(self):
        self.assertEqual(Solution().runningSum([1, 1, 1, 1, 1]), [1, 2, 3, 4, 5])

    def test_3(self):
        self.assertEqual(Solution().runningSum([3, 1, 2, 10, 1]), [3, 4, 6, 16, 17])


if __name__ == '__main__':
    unittest.main()
