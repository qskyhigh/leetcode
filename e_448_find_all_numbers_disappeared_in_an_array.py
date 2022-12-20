# https://leetcode.com/problems/find-smallest-letter-greater-than-target

from typing import List
import unittest
from dataclasses import dataclass


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        seen = set(nums)
        result = []
        n = len(nums)

        for i in range(1, n + 1):
            if i not in seen:
                result.append(i)

        return result


@dataclass
class TestCase:
    nums: List[int]
    expectation: List[int]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]),
            TestCase([1, 1], [2])
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.findDisappearedNumbers(t.nums), t.expectation)
