"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def gen_permute(l1, l2):
            if len(l2) == 0:
                result.append(l1)
                return
            else:
                for i in xrange(len(l2)):
                    tmp1, tmp2 = list(l1), list(l2)
                    tmp1.append(tmp2[i])
                    del tmp2[i]
                    gen_permute(tmp1, tmp2)

        gen_permute([], nums)
        return result


if __name__ == "__main__":
    assert Solution().permute([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ]
