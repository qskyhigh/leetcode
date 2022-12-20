# https://leetcode.com/problems/unique-number-of-occurrences

from typing import List
import unittest
from dataclasses import dataclass


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = dict()

        for i in arr:
            hashmap[i] = hashmap.get(i, 0) + 1
        if len(hashmap.values()) == len(set(hashmap.values())):
            return True
        return False


@dataclass
class TestCase:
    arr: List[int]
    expectation: bool


class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase([1, 2, 2, 1, 1, 3], True),
            TestCase([1, 2, 3], False),
            TestCase([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True)
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.uniqueOccurrences(t.arr), t.expectation)
