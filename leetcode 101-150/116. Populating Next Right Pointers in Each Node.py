"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL

"""


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect_1(self, root):
        if root is None:
            return
        current = [root]
        while current:
            next_level = []
            for node in current:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            if len(next_level) > 1:
                for i in xrange(len(next_level) - 1):
                    next_level[i].next = next_level[i + 1]

    def connect_2(self, root):
        if root is None:
            return
        if root.left:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

    def connect(self, root):
        head = root
        while head:
            curr = head
            while curr and curr.left:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            head = head.left


if __name__ == "__main__":
    tree_link_1 = TreeLinkNode(1)
    tree_link_1.left = TreeLinkNode(2)
    tree_link_1.left.left = TreeLinkNode(4)
    tree_link_1.left.right = TreeLinkNode(5)
    tree_link_1.right = TreeLinkNode(3)
    tree_link_1.right.left = TreeLinkNode(6)
    tree_link_1.right.right = TreeLinkNode(7)
    Solution().connect(tree_link_1)
    assert tree_link_1.left.next.val == tree_link_1.right.val
    assert tree_link_1.left.left.next.val == tree_link_1.left.right.val
    assert tree_link_1.left.right.next.val == tree_link_1.right.left.val
    assert tree_link_1.right.left.next.val == tree_link_1.right.right.val
