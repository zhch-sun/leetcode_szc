#
# @lc app=leetcode id=134 lang=python
#
# [134] Gas Station
#
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        part = 0
        total = 0
        start = 0
        for i in range(len(gas)):
            part += gas[i] - cost[i]
            if part < 0:
                total += part
                part = 0
                start = i + 1
        total += part
        return -1 if total < 0 else start
        
if __name__ == '__main__':
    """
    如下的答案更好理解, 这题不考
    https://leetcode.com/problems/gas-station/discuss/42648/My-one-pass-solution.
    维护当前start开始的和, 和总体的和. 
    重点在于, 当part开始为负时, part内部的值一定不是start!
    """
    s = Solution()
    print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))

