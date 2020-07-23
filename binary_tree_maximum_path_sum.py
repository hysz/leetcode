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


# At any node we have four options:
#   1. Route the longest path to the left.
#   2. Route the longest path to the right.
#   3. Halt the longest path at the current node.
#   4. Merge the left and right paths.
# We store stats below to represent these cases.
# extend - max value of cases 1-3 above. The parent will use its child's `extend` stat to extend their path downward.
# merge - value from case 4 above. This means that the path starts from the left, goes up to this node, then extends down the right.
# max_local - this is the max of extend and merge -- namely, what is the best option at this point?
# max_global - this is the global maximum path that we've found.
Stats = namedtuple('Sats', ['extend', 'merge', 'max_local', 'max_global'])

class Solution:

    # We work our way up from the bottom of the tree. At each step we record a bunch
    # of stats. See above for definitions.
    def run(self, node) -> Stats:
        if node == None:
            return Stats(0, 0, 0, -(pow(2,31)))

        # recurse
        left = self.run(node.left)
        right = self.run(node.right)

        # compute local stats
        extend = max(node.val, node.val + max(left.extend, right.extend))
        merge = node.val + left.extend + right.extend
        max_local = max(extend, merge)

        # update global max
        max_global = sorted([max_local, left.max_global, right.max_global])[-1]
        stats = Stats(extend, merge, max_local, max_global)  
        return stats      

    def maxPathSum(self, root: TreeNode) -> int:
        stats = self.run(root)
        return stats.max_global



print(Solution().maxPathSum(TreeNode(9, TreeNode(6), TreeNode(-3, TreeNode(-6), TreeNode(2, TreeNode(2, TreeNode(-6, TreeNode(-6)), TreeNode(-6)))))))


#print(Solution().maxPathSum(TreeNode(9, TreeNode(6), TreeNode(-3, TreeNode(-6), TreeNode(2, TreeNode(2, TreeNode(-6, TreeNode(-6), TreeNode(-6))))))))



#print(Solution().maxPathSum(TreeNode(2, TreeNode(-1), TreeNode(-2))))
#print(Solution().maxPathSum(TreeNode(-2, TreeNode(-1))))
#print(Solution().maxPathSum(TreeNode(1, TreeNode(2))))
#print(Solution().maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))))
#print(Solution().maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))



        