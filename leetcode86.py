# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less = ListNode(-1)
        more = ListNode(-2)

        l = less
        m = more

        p = head
        while p:
            if p.val < x:
                l.next = p
                l = p
            else:
                m.next = p
                m = p
            p = p.next

        m.next = None

        l.next = more.next
        return less.next

if __name__ == '__main__':
    S = Solution()
    a = ListNode(1)
    print(S.partition(head=a, x=2).val)




        