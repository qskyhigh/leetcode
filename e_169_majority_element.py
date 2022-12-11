# https://leetcode.com/problems/majority-element

from typing import List
import unittest
from dataclasses import dataclass

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = dict()
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        return max(hash_map.keys(), key=hash_map.get)

class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        max_element = len(nums) // 2
        for num in nums:
            count = sum(1 for elem in nums if num == elem)
            if count > max_element:
                return num

@dataclass
class TestCase:
    nums: List[int]
    expectation: int

class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase([3, 2, 3], 3),
            TestCase([2, 2, 1, 1, 1, 2, 2], 2)
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.majorityElement(t.nums), t.expectation)
