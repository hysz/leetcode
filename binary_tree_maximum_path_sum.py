import sys
from collections import namedtuple

class TreeNode:
    val = 0
    left = None
    right = None

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

Stats = namedtuple('Sats', ['single', 'combined', 'max_local', 'max_global'])

class Solution:

    def run(self, node) -> Stats:
        if node == None:
            return Stats(0, 0, 0, -(pow(2,31)))

        # recurse
        left = self.run(node.left)
        right = self.run(node.right)

        #print(left)
        #print(right)

        # compute local stats
        single = node.val + max(left.single, right.single)
        combined = node.val + left.single + right.single
        max_local = sorted([single, combined, node.val])[-1]

        # update global max
        max_global = sorted([max_local, left.max_global, right.max_global])[-1]
        return Stats(single, combined, max_local, max_global)        

    def maxPathSum(self, root: TreeNode) -> int:
        stats = self.run(root)
        return stats.max_global



print(Solution().maxPathSum(TreeNode(2, TreeNode(-1), TreeNode(-2))))
#print(Solution().maxPathSum(TreeNode(-2, TreeNode(-1))))
#print(Solution().maxPathSum(TreeNode(1, TreeNode(2))))
#print(Solution().maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))))
#print(Solution().maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))



        