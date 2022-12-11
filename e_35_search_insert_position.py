# https://leetcode.com/problems/search-insert-position/
from typing import List
import unittest
from dataclasses import dataclass

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            if guess > target:
                high = mid - 1
            else:
                low = mid + 1
        if nums[mid] > target:
            return mid
        else:
            return mid + 1

@dataclass
class TestCase:
    nums: List[int]
    target: int
    expectation: int


class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase([1, 3, 5, 6], 5, 2),
            TestCase([1, 3, 5, 6], 2, 1),
            TestCase([1, 3, 5, 6], 7, 4)
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.searchInsert(t.nums, t.target), t.expectation)
