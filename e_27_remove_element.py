# https://leetcode.com/problems/remove-element
from typing import List
import unittest
from dataclasses import dataclass

# Solution 1
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         index = 0
#         for i in range(len(nums)):
#             if nums[i] != val and nums[index] == val:
#                 nums[index], nums[i] = nums[i], nums[index]
#
#             if nums[index] != val:
#                 index += 1
#         return index

# Solution 2
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

@dataclass
class TestCase:
    nums: list
    val: int
    expectation: int

class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase([3, 2, 2, 3], 3, 2),
            TestCase([0, 1, 2, 2, 3, 0, 4, 2], 2, 5)
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.removeElement(t.nums, t.val),t.expectation)