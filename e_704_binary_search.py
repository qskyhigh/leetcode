# https://leetcode.com/problems/binary-search

from typing import List
import unittest
from dataclasses import dataclass

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

@dataclass
class TestCase:
    nums: List[int]
    target: int
    expectation: int

class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase([-1, 0, 3, 5, 9, 12], 9, 4),
            TestCase([-1, 0, 3, 5, 9, 12], 2, -1)
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.search(t.nums, t.target), t.expectation)
