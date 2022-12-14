# https://leetcode.com/problems/find-smallest-letter-greater-than-target

from typing import List
import unittest
from dataclasses import dataclass

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[len(letters) - 1] <= target or target < letters[0]:
            return letters[0]

        low = 0
        high = len(letters) - 1

        while low <= high:
            mid = (high + low) // 2

            if letters[mid] > target:
                high = mid - 1
            elif letters[mid] <= target:
                low = mid + 1

        if letters[high] <= target:
            return letters[high + 1]
        else:
            return letters[high]

class Solution2(object):
    def nextGreatestLetter(self, letters, target):
        for c in letters:
            if c > target:
                return c
        return letters[0]

@dataclass
class TestCase:
    letters: List[str]
    target: str
    expectation: str

class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase(["c", "f", "j"], "a", "c"),
            TestCase(["c", "f", "j"], "c", "f"),
            TestCase(["x", "x", "y", "y"], "z", "x")
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.nextGreatestLetter(t.letters, t.target), t.expectation)
