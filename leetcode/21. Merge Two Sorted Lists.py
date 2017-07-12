# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        result = dummy
        while l1 or l2:
            if not l1:
                dummy.next = ListNode(l2.val)
                l2 = l2.next
            elif not l2:
                dummy.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val > l2.val:
                dummy.next = ListNode(l2.val)
                l2 = l2.next
            else:
                dummy.next = ListNode(l1.val)
                l1 = l1.next
            dummy = dummy.next
        return result.next


if __name__ == "__main__":
    l1 = ListNode(2)
    l2 = ListNode(1)
    result = Solution().mergeTwoLists(l1, l2)
    assert result.val == 1
    assert result.next.val == 2

    l1, l1.next, l1.next.next = ListNode(1), ListNode(3), ListNode(5)
    l2, l2.next, l2.next.next = ListNode(2), ListNode(4), ListNode(6)
    result = Solution().mergeTwoLists(l1, l2)
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next.val == 3
    assert result.next.next.next.val == 4
    assert result.next.next.next.next.val == 5
    assert result.next.next.next.next.next.val == 6





