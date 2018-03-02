# Definition for singly-linked list.

import queue

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        Q = queue.PriorityQueue(len(lists))

        pre = ListNode(-1)
        r = pre
        pointers = list()
        for list_ in lists:
            if list_:
                pointers.append(list_)

        while 1:
            min_num = 1000
            min_p = None
            min_i = -1

            if len(pointers) == 0:
                break

            for i, p in enumerate(pointers):
                if p.val < min_num:
                    min_num = p.val
                    min_p = p
                    min_i = i
            r.next = min_p
            r = min_p
            pointers[min_i] = min_p.next

            new_pointers = list()
            for p in pointers:
                if p:
                    new_pointers.append(p)
            pointers = new_pointers

        return pre.next

if __name__ == '__main__':
    a1 = ListNode(1)
    a4 = ListNode(4)
    a6 = ListNode(6)

    b0 = ListNode(0)
    b5 = ListNode(5)
    b7 = ListNode(7)

    c1 = ListNode(1)
    c3 = ListNode(3)

    a1.next = a4
    a4.next = a6
    b0.next = b5
    b5.next = b7

    c1.next = c3

    S =Solution()
    d = S.mergeKLists([a1, b0, c1])
    while d:
        print(d.val)
        d = d.next



