#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#

# class MinStack(object):

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.s = []
#         self.mini= [float('inf')]
        
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: None
#         """
#         if x <= self.mini[-1]:
#             self.mini.append(x)
#         self.s.append(x)

#     def pop(self):
#         """
#         :rtype: None
#         """
#         # check if empty stack?
#         x = self.s.pop()
#         if x == self.mini[-1]:
#             self.mini.pop()
#         return x

#     def top(self):
#         """
#         :rtype: int
#         """
#         # check if empty stack?
#         return self.s[-1]

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.mini[-1]



class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.mini = float('inf')
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x <= self.mini:
            self.s.append(self.mini)
            self.mini = x
        self.s.append(x)

    def pop(self):
        """
        :rtype: None
        """
        x = self.s.pop()
        if x == self.mini:
            self.mini = self.s.pop()
        return x

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == '__main__':
    """
    可以用一个额外的stack存着历次min的值.
    也可以用一个stack实现. 最简单的是当push改变min时push两个, pop改变min时pop两次. 
    """
    s = MinStack()
