"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon.
The dungeon consists of M x N rooms laid out in a 2D grid.
Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon
to rescue the princess.

The knight has an initial health point represented by a positive integer.
If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons,
so the knight loses health (negative integers) upon entering these rooms;
other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible,
the knight decides to move only rightward or downward in each step.

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below,
the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2(K)   -3      3
-5      -10     1
10      30      -5 (P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups,
even the first room the knight enters and the bottom-right room where the princess is imprisoned.

Credits:
Special thanks to @stellari for adding this problem and creating all test cases.

"""


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        hp = [[0 for _ in xrange(n)] for _ in xrange(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 == m and j + 1 == n:
                    hp[i][j] = 1
                elif i + 1 == m:
                    hp[i][j] = max(hp[i][j + 1] - dungeon[i][j + 1], 1)
                elif j + 1 == n:
                    hp[i][j] = max(hp[i + 1][j] - dungeon[i + 1][j], 1)
                else:
                    hp[i][j] = max(min(hp[i + 1][j] - dungeon[i + 1][j], hp[i][j + 1] - dungeon[i][j + 1]),
                                   1)

        return max(hp[0][0] - dungeon[0][0], 1)


if __name__ == "__main__":
    assert Solution().calculateMinimumHP([[100]]) == 1
    assert Solution().calculateMinimumHP([[0, 0]]) == 1
    assert Solution().calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]) == 7
