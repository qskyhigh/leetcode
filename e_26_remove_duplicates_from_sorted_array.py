# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List
import unittest
from dataclasses import dataclass

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)

        current_index = 1
        for i in range(1, size):
            if nums[i - 1] != nums[i]:
                nums[current_index] = nums[i]
                current_index += 1
        return current_index

@dataclass
class TestCase:
    nums: list
    expectation: int

class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase([1, 1, 2], 2),
            TestCase([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5)
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.removeDuplicates(t.nums), t.expectation)
