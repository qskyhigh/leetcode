# https://leetcode.com/problems/merge-sorted-array

from typing import List
import unittest
from dataclasses import dataclass

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.__class__.__name__}(val={self.val}, next={self.next})'


def list_to_listnode(int_list: Optional[List[int]]) -> Optional[ListNode]:
    if not int_list:
        return None

    node = None

    for i in reversed(int_list):
        node = ListNode(i, node)

    return node


def listnode_to_list(list_node: Optional[ListNode]) -> Optional[List[int]]:
    if not list_node:
        return []

    if not list_node.next:
        return [list_node.val]

    node = list_node
    result = []

    while node:
        result.append(node.val)
        node = node.next

    return result


class Solution:
    @staticmethod
    def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = current = ListNode()

        if not list1 and not list2:
            return list1

        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return dummy.next


@dataclass
class TestCase:
    list1: Optional[ListNode]
    list2: Optional[ListNode]
    expectation: Optional[ListNode]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase(list1=[], list2=[], expectation=[]),
            TestCase(list1=[], list2=[0], expectation=[0]),
            TestCase(list1=[1, 2, 4], list2=[1, 3, 4], expectation=[1, 1, 2, 3, 4, 4]),
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(listnode_to_list(solution.merge_two_lists(list_to_listnode(t.list1), list_to_listnode(t.list2))), t.expectation)
