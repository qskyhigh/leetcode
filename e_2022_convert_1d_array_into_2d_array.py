# https://leetcode.com/problems/convert-1d-array-into-2d-array

from typing import List
import unittest
from dataclasses import dataclass


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = []
        if m * n != len(original):
            return []

        for i in range(0, len(original), n):
            result.append(original[i:i + n])

        return result


@dataclass
class TestCase:
    nums: List[int]
    m: int
    n: int
    expectation: List[int]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase([1, 2, 3, 4], 2, 2, [[1, 2], [3, 4]]),
            TestCase([1, 2, 3], 1, 3, [[1, 2, 3]])
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.construct2DArray(t.nums, t.m, t.n), t.expectation)
