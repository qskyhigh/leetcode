# https://leetcode.com/problems/move-zeroes/
from typing import List
import unittest
from dataclasses import dataclass

# 283. Move Zeroes https://leetcode.com/problems/move-zeroes/
# Input: nums = [0,1,0,3,12] Output: [1,3,12,0,0]

# Solution 1
class Solution1:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        if len(nums) == 1 and nums[0] == 0:
            return nums

        cnt = 0
        index = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
            else:
                nums[index] = nums[i]
                index += 1

        for i in range(1, cnt + 1):
            nums[-i] = 0
        return nums

# Solution 2
class Solution2:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1
        return nums

@dataclass
class TestCase:
    nums: List[int]
    expectation: List[int]

class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution2()

        tests = [
            TestCase(nums=[0, 1, 0, 3, 12], expectation=[1, 3, 12, 0, 0])
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.moveZeroes(t.nums), t.expectation)
