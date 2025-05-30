class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 构建树结构
'''
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
'''

# 节点
n3 = TreeNode(3)
n5 = TreeNode(5)
n1 = TreeNode(1)
n6 = TreeNode(6)
n2 = TreeNode(2)
n0 = TreeNode(0)
n8 = TreeNode(8)
n7 = TreeNode(7)
n4 = TreeNode(4)

# 构建连接
n3.left = n5
n3.right = n1
n5.left = n6
n5.right = n2
n2.left = n7
n2.right = n4
n1.left = n0
n1.right = n8


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right


s = Solution()
lca = s.lowestCommonAncestor(n3, n6, n0)
print(f"最近公共祖先是: {lca.val}")
