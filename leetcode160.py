# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        len_a = 0
        len_b = 0
        p = headA
        while p:
            len_a += 1
            p = p.next
        p = headB
        while p:
            len_b += 1
            p = p.next

        print(len_a, len_b)

        p = headA
        q = headB
        if len_a >= len_b:
            diff = len_a - len_b
            while diff > 0:
                p = p.next
                diff -= 1
        else:
            diff = len_b - len_a
            while diff > 0:
                q = q.next
                diff -= 1

        while p != q and p:
            p = p.next
            q = q.next

        return p

if __name__ == '__main__':
    S = Solution()
    a1 = ListNode("a1")
    a2 = ListNode("a2")
    c1 = ListNode("c1")
    c2 = ListNode("c2")
    c3 = ListNode("c3")
    b1 = ListNode("b1")
    b2 = ListNode("b2")
    b3 = ListNode("b3")

    a1.next = a2
    a2.next = c1
    c1.next = c2
    c2.next = c3
    b1.next = b2
    b2.next = b3
    b3.next = c1

    print(S.getIntersectionNode(a1, b1).val)