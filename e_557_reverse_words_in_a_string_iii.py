# https://leetcode.com/problems/reverse-words-in-a-string-iii/
from typing import List
import unittest
from dataclasses import dataclass

# 557. Reverse Words in a String III
# Input: s = "Let's take LeetCode contest" Output: "s'teL ekat edoCteeL tsetnoc"
# Input: s = "God Ding" Output: "doG gniD"

class Solution:
    def reverseWords(self, s: str) -> str:
        reverse_s = []

        for word in s.split():
            reverse_word = ''
            for i in range(len(word), 0, -1):
                reverse_word += word[i - 1]
            reverse_s.append(reverse_word)
        return ' '.join(reverse_s)

@dataclass
class TestCase:
    s: str
    expectation: str

class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase(s="Let's take LeetCode contest", expectation="s'teL ekat edoCteeL tsetnoc"),
            TestCase(s="God Ding", expectation="doG gniD")
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.reverseWords(t.s), t.expectation)