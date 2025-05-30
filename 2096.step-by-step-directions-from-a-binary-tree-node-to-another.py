#
# @lc app=leetcode id=2096 lang=python3
#
# [2096] Step-By-Step Directions From a Binary Tree Node to Another
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        startPath = []
        foundStartPath = self.findPath(root, startPath, target=startValue)
        destPath = []
        foundDestPath = self.findPath(root, destPath, target=destValue)

        if not foundStartPath or not foundDestPath:
            return ""

        i = 0
        while i < min(len(startPath), len(destPath)):
            if startPath[i] != destPath[i]:
                break
            i += 1
        # [UUUUUUU]
        return "".join(['U'] * (len(startPath) - i) + destPath[i:])

    def findPath(self, node, path, target):
        # base case
        if not node:
            return False
        if node.val == target:
            return True

        # recursive call

        # go left
        path.append("L")
        left = self.findPath(node.left, path, target)
        if left:
            return True
        # 还原
        path.pop()

        path.append("R")
        right = self.findPath(node.right, path, target)
        if right:
            return True
        path.pop()

        # cannot find
        return False


# @lc code=end
