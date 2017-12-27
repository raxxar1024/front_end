"""
Given an integer, write a function to determine if it is a power of two.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        shift = 1
        while n >= shift:
            if n & shift:
                count += 1
            shift <<= 1
        return count == 1


if __name__ == "__main__":
    assert Solution().isPowerOfTwo(4) is True
    assert Solution().isPowerOfTwo(5) is False
