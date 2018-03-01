# Definition for singly-linked list.
# leetcode206.py

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count = 0
        fake_head = ListNode(-1)
        fake_head.next = head
        pointer = fake_head
        while 1:
            if count < m - 1:
                pointer = pointer.next
            if count == m - 1:
                p = pointer
                tail = p.next
                q = tail.next
            if count in range(m, n):
                a = p.next
                p.next = q
                tail.next = q.next
                q.next = a
                q = tail.next
            if count > n:
                break
            count = count + 1

        return fake_head.next

if __name__ == "__main__":
    ln1 = ListNode(1)
    ln2 = ListNode(2)
    ln3 = ListNode(3)
    ln4 = ListNode(4)
    ln5 = ListNode(5)
    ln1.next = ln2
    ln2.next = ln3
    ln3.next = ln4
    ln4.next = ln5

    sol = Solution()
    head = sol.reverseBetween(ln1, 1, 3)
    c = head
    while c:
        print(c.val)
        c = c.next
