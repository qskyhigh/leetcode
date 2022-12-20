# https://leetcode.com/problems/find-smallest-letter-greater-than-target

from typing import List
import unittest
from dataclasses import dataclass


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        result = []

        def binary_search(arr: List[int], target: int) -> bool:
            low, high = 0, len(arr) - 1

            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return True
                if arr[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return False

        for num in arr1:
            if binary_search(arr2, num) and binary_search(arr3, num):
                result.append(num)
        return result


class Solution2:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        hashmap = {}

        for num in arr1:
            if num not in hashmap:
                hashmap[num] = 1

        for num in arr2:
            if num in hashmap and hashmap[num] == 1:
                hashmap[num] = 2

        for num in arr3:
            if num in hashmap and hashmap[num] == 2:
                hashmap[num] = 3

        result = []
        for k, v in hashmap.items():
            if v == 3:
                result.append(k)
        return result

@dataclass
class TestCase:
    arr1: List[int]
    arr2: List[int]
    arr3: List[int]
    expectation: List[int]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase([1, 2, 3, 4, 5], [1, 2, 5, 7, 9], [1, 3, 4, 5, 8], [1, 5]),
            TestCase([197, 418, 523, 876, 1356], [501, 880, 1593, 1710, 1870], [521, 682, 1337, 1395, 1764], [])
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.arraysIntersection(t.arr1, t.arr2, t.arr3), t.expectation)
