"""
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j]
and the absolute difference between i and j is at most k.

"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lookup = {}
        for i, num in enumerate(nums):
            if num in lookup and i - lookup[num] <= k:
                return True
            lookup[num] = i
        return False


if __name__ == "__main__":
    assert Solution().containsNearbyDuplicate([1, 2, 3, 1, 2], 3) is True
