"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.

Credits:
Special thanks to @mithmatt for adding this problem, creating the above image and all test cases.

"""


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        return (C - A) * (D - B) + (G - E) * (H - F) - \
               max(0, min(C, G) - max(A, E)) * max(0, min(D, H) - max(B, F))


if __name__ == "__main__":
    assert Solution().computeArea(0, 0, 0, 0, -1, -1, 1, 1) == 4
    assert Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2) == 45
    assert Solution().computeArea(-2, -2, 2, 2, -2, -2, 2, 2) == 16
