#
# @lc app=leetcode id=145 lang=python
#
# [145] Binary Tree Postorder Traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def postorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     def helper(root, ans):
    #         if not root:
    #             return
    #         helper(root.left, ans)
    #         helper(root.right, ans)
    #         ans.append(root.val)
    #     ans = []
    #     helper(root, ans)
    #     return ans

    def postorderTraversal(self, root):
        def helper(root, ans):
            if not root:
                return
            ans.append(root.val)
            helper(root.right, ans)
            helper(root.left, ans)
        ans = []
        helper(root, ans)
        return reversed(ans)

if __name__ == '__main__':
    """
    解法1: 递归
    解法2: 转换成preorder
        left right root 是preorder倒过来, root, right, left
    解法3: 不写了. 
        第一个回复给出了一个general的三种traversal. 需要用一个last_pop来判断位置. 
        https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45559/My-Accepted-code-with-explaination.-Does-anyone-have-a-better-idea
        下面的不需要pre pointer
        https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45551/Preorder-Inorder-and-Postorder-Iteratively-Summarization/44991
    解法4:
        这个blog也不错. 还有morris.
        https://techgeekyan.blogspot.com/2017/08/leetcode-145-binary-tree-postorder.html 
    """
    s = Solution()
