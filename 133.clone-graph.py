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
        self.neighbors = neighbors
# """
class Solution(object):
    # def cloneGraph(self, node):
    #     """
    #     :type node: Node
    #     :rtype: Node
    #     """
    #     # 正常dfs
    #     # def helper(node):
    #     #     # dfs逻辑2: 在for循环内部check是否在memo里
    #     #     memo[node] = Node(node.val, [])
    #     #     for item in node.neighbors:
    #     #         # 这里不能用default简化逻辑, 也没法用defaultdict? 因为不能绑参数? 
    #     #         new_item = memo.get(item) or helper(item)  # 卧槽是or不是and...
    #     #         memo[node].neighbors.append(new_item)
    #     #     return memo[node]

    #     def helper(node):
    #         # dfs逻辑1: 函数入口处check是否已经在memo里
    #         if node not in memo:
    #             memo[node] = Node(node.val, [])
    #             memo[node].neighbors = [helper(item) for item in node.neighbors]
    #         return memo[node]
    #     if not node:
    #         return
    #     memo = {}
    #     return helper(node)

    # def cloneGraph(self, node):
    #     # dfs最短代码, list comprehension + and trick + or trick
    #     def helper(node, memo):
    #         new_node = memo[node] = Node(node.val, [])
    #         # 这一句不能合并到前面去, 因为需要更新过的memo; 另外注意是or不是and!!
    #         new_node.neighbors = [memo.get(item) or helper(item, memo) for item in node.neighbors]
    #         return new_node
    #     memo = {}
    #     return node and helper(node, memo)  # and trick
        
    def cloneGraph(self, node):
        # dfs iteratively
        if not node:
            return
        stack = [node]  # store unique nodes
        new_head = Node(node.val, [])
        memo = {node: new_head}
        while stack:
            node = stack.pop()
            new_node = memo.get(node) or Node(node.val, [])
            for item in node.neighbors:
                new_item = memo.get(item)
                if new_item is None:
                    stack.append(item)
                    new_item = Node(item.val, [])
                    memo[item] = new_item  # 忘记了这里..
                new_node.neighbors.append(new_item)
        return new_head


if __name__ == '__main__':
    """
    对于一个连通(?)的无向无环图, 返回该图的deep copy
        note: 该图是简单图, 没有重复的edge和环
        因为是无向图, p如果有neighbor q, 则q也有neighbor p. 
    dfs recursive:
        因为是无向图, 连接是双向的. 所以需要搞一个dict来记录谁之前的node:new_node pair
        如果node已经被创建, 则不能再递归! 否则死循环
        两种实现: 第一种解法, 函数入口处check更合理一些.
        递归时调错函数了...调成了主函数..结果一直debug. 
    dfs iterative:
        有个python答案, 但是具体实现其实还是bfs... 尽管是个stack..
        所以好像没有简单的dfs iterative. 有一个dfs如下,非常复杂
        https://leetcode.com/problems/clone-graph/discuss/42342/Depth-First-Iterative-C%2B%2B-solution
    bfs with stack:
        注意当memo中找不到时需要很多操作...
    """
    s = Solution()

