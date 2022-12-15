# https://leetcode.com/problems/merge-sorted-array

from typing import List
import unittest
from dataclasses import dataclass
from functools import wraps
import time

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} Took {total_time:.8f} seconds')
        return result
    return timeit_wrapper
class Solution:

    @timeit
    def binary_search(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            low = 0
            high = len(numbers) - 1
            while low <= high:
                mid = (high + low) // 2
                if numbers[mid] == target - numbers[i] and mid != i:
                    return [i + 1, mid + 1]
                if numbers[mid] > target - numbers[i]:
                    high = mid - 1
                else:
                    low = mid + 1

    # two-pointer
    @timeit
    def two_pointer(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1

    # dictionary
    @timeit
    def dictionary(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            dic[num] = i

@dataclass
class TestCase:
    numbers: List[int]
    target: int
    expectation: List[int]

class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase([2, 7, 11, 15], 9, [1, 2]),
            TestCase([2, 3, 4], 6, [1, 3]),
            TestCase([-1, 0], -1, [1, 2]),
            TestCase([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5])
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.binary_search(t.numbers, t.target), t.expectation)
                self.assertEqual(solution.two_pointer(t.numbers, t.target), t.expectation)
                self.assertEqual(solution.dictionary(t.numbers, t.target), t.expectation)
