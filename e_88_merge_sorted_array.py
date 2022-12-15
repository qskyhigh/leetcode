# https://leetcode.com/problems/merge-sorted-array

from typing import List
import unittest
from dataclasses import dataclass

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
        return nums1

@dataclass
class TestCase:
    nums1: List[int]
    m: int
    nums2: List[int]
    n: int
    expectation: List[int]

class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
            TestCase([1], 1, [], 0, [1]),
            TestCase([0], 0, [1], 1, [1])
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.merge(t.nums1, t.m, t.nums2, t.n), t.expectation)
