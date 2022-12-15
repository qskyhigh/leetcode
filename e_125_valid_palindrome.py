# https://leetcode.com/problems/valid-palindrome

# https://leetcode.com/problems/merge-sorted-array

from typing import List
import unittest
from dataclasses import dataclass

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        old_s = ''.join(i.lower() for i in s if i.isalnum())
        return old_s == old_s[::-1]

@dataclass
class TestCase:
    s: str
    expectation: bool

class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase("A man, a plan, a canal: Panama", True),
            TestCase("race a car", False),
            TestCase(" ", True)
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.isPalindrome(t.s), t.expectation)
