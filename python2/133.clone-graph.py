#
# @lc app=leetcode id=133 lang=python
#
# [133] Clone Graph
#
# """
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors  # list of node
# """
class Solution(object):
   def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        def dfs(node):
            # dfs逻辑1: 函数入口处check是否已经在memo里
            if node not in memo:
                memo[node] = Node(node.val, [])
                memo[node].neighbors = [dfs(item) for item in node.neighbors]
            return memo[node]
        if not node:
            return
        memo = {}
        return dfs(node)    

    # def cloneGraph(self, node):
    #     # bfs 
    #     from collections import deque
    #     if not node:
    #         return
    #     memo = {node: Node(node.val, [])}
    #     dq = deque([node])
    #     while dq:
    #         n1 = dq.popleft()  # Note memo[n1]一定存在
    #         for x in n1.neighbors:
    #             if x not in memo:
    #                 memo[x] = Node(x.val, [])
    #                 dq.append(x)  # Note 不是nx! 注意位置
    #             memo[n1].neighbors.append(memo[x])  # 这里nx
    #     return memo[node]

    # def cloneGraph(self, head):
    #     # dfs iteratively
    #     if not head:
    #         return
    #     stack = [head]  # store unique nodes
    #     memo = {head: Node(head.val, [])}
    #     while stack:
    #         node = stack.pop()  # memo[node]一定存在
    #         for item in node.neighbors:
    #             if item not in memo:
    #                 stack.append(item)
    #                 memo[item] = Node(item.val, [])
    #             memo[node].neighbors.append(memo[item])
    #     return memo[head]


if __name__ == '__main__':
    """
    题设: 对于一个连通的无向有环图, 返回该图的deep copy
        note: 该图是简单图, 没有平行边和自环
        因为是无向图, p如果有neighbor q, 则q也有neighbor p. 
    解法1:
        有关爆栈问题, 图比链表还是弱一点. 一般不太可能递归到1000.
        递归最简单. 
    解法2:
        bfs迭代. 注意写法. 这种复制题没必要给新的item一个变量
        直接用memo[x]即可. 
        注意dq中存x, memo中存nx..
    解法3:
        dfs迭代. 直接把上面的queue变成stack即可. 
    """
    s = Solution()

