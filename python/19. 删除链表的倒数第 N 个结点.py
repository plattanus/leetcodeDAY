# Definition for singly-linked list.
# from typing import Optional


# from argparse import OPTIONAL


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: OPTIONAL[ListNode], n: int) -> Optional[ListNode]:

        def getLength(thead: ListNode) -> int:
            length = 0
            while thead:
                thead = thead.next
                length += 1
            return length

        length = getLength(head)

        if length == n:
            # if n == 1:
            head = head.next
            return head

        index = length - n

        phead = ListNode(0, head)
        
        for i in range(index):
            phead = phead.next
        phead.next = phead.next.next
        return head

if __name__  == '__main__':
    head = [1,2,3,4,5]
    n = 2
    head = [1]
    n = 1
    head = [1,2]
    n = 1
    rtn = Solution().removeNthFromEnd(head, n)
    print(rtn)
