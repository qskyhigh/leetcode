# https://leetcode.com/problems/find-smallest-letter-greater-than-target

from typing import List
import unittest
from dataclasses import dataclass

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n):
            idx = n - 1 - i

            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits

        return [1] + digits

@dataclass
class TestCase:
    digits: List[int]
    expectation: List[int]

class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase([1, 2, 3], [1, 2, 4]),
            TestCase([2, 3, 9], [2, 4, 0]),
            TestCase([9, 9, 9], [1, 0, 0, 0])
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.plusOne(t.digits), t.expectation)
