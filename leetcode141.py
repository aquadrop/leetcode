# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head or not head.next:
            return False

        p = head.next
        q = head

        p = p.next
        if p == q:
            return True

        while p and q and p.next and p.next.next:
            q = q.next
            p = p.next
            if p == q:
                return True
            p = p.next
        return False

if __name__ == '__main__':
    S = Solution()
    a1 = ListNode("a1")
    a2 = ListNode("a2")
    a3 = ListNode("a3")
    a4 = ListNode("a4")
    a5 = ListNode("a5")
    # a1.next = a2
    # a2.next = a3
    # a3.next = a4
    # a4.next = a5
    # a5.next = a1


    print(S.hasCycle(a1))