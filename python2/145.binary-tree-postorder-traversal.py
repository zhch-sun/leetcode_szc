#
# @lc app=leetcode id=145 lang=python
#
# [145] Binary Tree Postorder Traversal
#
def listToTree(input):
    if not input:
        return None
    root = TreeNode(int(input[0]))
    nodeQueue = [root]  # 最后这个包含所有node
    front = 0  # to index queue
    index = 1  # to index list
    while index < len(input):
        node = nodeQueue[front]
        front += 1

        left_num = input[index]
        if left_num is not None:
            # 这意味着前面的None会使后面的位置直接跳过
            node.left = TreeNode(left_num)
            nodeQueue.append(node.left)

        index += 1
        if index >= len(input):
            break

        right_num = input[index]
        if right_num is not None:
            node.right = TreeNode(right_num)
            nodeQueue.append(node.right)
        index += 1
    return root

def treeToList(input):
    if not input:
        return None
    cur = input
    nodeQueue = [cur]
    res = []
    front = 0
    while True:
        val = cur.val if cur is not None else None
        res.append(val)
        if cur is not None:  #及时该位置是空的，也要None?
            nodeQueue.append(cur.left)
            nodeQueue.append(cur.right)
        front += 1
        if front < len(nodeQueue):
            cur = nodeQueue[front]
        else:
            break
    while res[-1] is None:  # 符合定义?
        res.pop()
    return res

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
        # return reversed(ans)
        return ans[::-1]

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
    print(s.postorderTraversal(listToTree([1,2,3,None,5,6,7])))
    print(s.postorderTraversal(listToTree([1,2,3,5,None,6,7])))
