# https://leetcode.com/problems/summary-ranges/
from typing import List
import unittest
from dataclasses import dataclass

# 228. Summary Ranges https://leetcode.com/problems/summary-ranges/
# Input: nums = [0,1,2,4,5,7] Output: ["0->2","4->5","7"]

# Solution 1
class Solution1:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        index = 0
        for i, v in enumerate(nums):
            if i == len(nums) - 1 or nums[i + 1] - nums[i] > 1:
                result.append(str(nums[index]) + '->' + str(v) if nums[index] != v else str(v))
                index = i + 1

        return result

# Solution 2
class Solution2:
    def summaryRanges(nums):
        ranges, r = [], []
        for n in nums:
            if n - 1 not in r:
                r = []
                ranges += r,
            r[1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]

@dataclass
class TestCase:
    nums: List[int]
    expectation: List[str]

class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution1()

        tests = [
            TestCase(nums=[0, 1, 2, 4, 5, 7], expectation=['0->2', '4->5', '7'])
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.summaryRanges(t.nums), t.expectation)