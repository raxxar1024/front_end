"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """


if __name__ == "__main__":
    print Solution().numTrees(3) == 5
