# https://leetcode.com/problems/reverse-integer
from typing import List
import unittest
from dataclasses import dataclass

class Solution:
    def reverse(self, x: int) -> int:
        if x // 10 == 0:
            return x
        new_x = 0
        old_x = abs(x)
        while old_x > 0:
            new_x = new_x*10 + old_x%10
            old_x = old_x // 10
        if x > 0:
            if new_x > (2**31) - 1:
                return 0
            return new_x
        else:
            if -new_x < -(2**31):
                return 0
            return -new_x

@dataclass
class TestCase:
    num: int
    expectation: int

class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase(123, 321),
            TestCase(-123, -321),
            TestCase(120, 21)
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.reverse(t.num), t.expectation)
