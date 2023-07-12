# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t = 0
        l3 = ListNode()
        n = l3
        while True:
            if l1:
                t += l1.val
                l1 = l1.next
            if l2:
                t += l2.val
                l2 = l2.next
            n.val = t%10
            t //= 10
            if not l1 and not l2:
                break
            n.next = ListNode()
            n = n.next
        if t != 0:
            n.next = ListNode()
            n = n.next
            n.val = t
            n.next = None
        return l3

if __name__  == '__main__':
    l1 = [2,4,3]
    l2 = [5,6,4]
    rtn = Solution().addTwoNumbers(l1, l2)
    print(rtn)