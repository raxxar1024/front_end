"""
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """


if __name__ == "__main__":
    assert Solution().hIndex([0]) == 0
    assert Solution().hIndex([100]) == 1
    assert Solution().hIndex([1]) == 1
    assert Solution().hIndex([0, 1, 3, 5, 6]) == 3
