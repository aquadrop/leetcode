# Definition for singly-linked list.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None

        dict1 = {}
        dict2 = {}

        fh1 = RandomListNode(0)
        fh2 = RandomListNode(0)

        fh1.next = head
        p = head
        q = fh2

        _id_ = 0
        while p:
            a = RandomListNode(p.label)
            q.next = a
            q = a

            dict1[p] = _id_
            dict2[_id_] = a
            _id_ += 1
            p = p.next

        p = head
        new_head = fh2.next
        q = new_head
        while p:
            if p.random:
                _id_ = dict1[p.random]
                a = dict2[_id_]
                q.random = a
            p = p.next
            q = q.next

        return new_head





        