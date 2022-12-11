# https://leetcode.com/problems/majority-element-ii

from typing import List
import unittest
from dataclasses import dataclass

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [num for num in set(nums) if nums.count(num) > len(nums) // 3]

class Solution2:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_map = dict()
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        return [k for k, v in hash_map.items() if v > len(nums) // 3]

@dataclass
class TestCase:
    nums: List[int]
    expectation: List[int]

class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase([3, 2, 3], [3]),
            TestCase([2, 2, 1, 1, 1, 2, 2], [1, 2]),
            TestCase([1, 2], [1, 2])
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.majorityElement(t.nums), t.expectation)
