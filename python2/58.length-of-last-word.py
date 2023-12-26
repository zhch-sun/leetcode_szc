#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#
class Solution(object):
    # def lengthOfLastWord(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     # This use linear memory
    #     # strip也会用O(n)的时间...而且还有copy的O(n)时间
    #     return len(s.rstrip().split(' ')[-1])
    
    def lengthOfLastWord(self, s):
        if not s:
            return 0
        tail = len(s) - 1
        while tail >= 0 and s[tail].isspace():  # Note this function
            tail -= 1
        cnt = 0
        while tail >=0 and not s[tail].isspace():
            tail -=1
            cnt +=1
        return cnt       

    # def lengthOfLastWord(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     # 合并while loop, 不如前面的清晰易懂
    #     if not s:
    #         return 0
    #     count = 0  # number of word
    #     cur = 0  # cur length
    #     pre = 0  # pre length
    #     for i in range(len(s)):
    #         if cur != 0 and s[i] == ' ':
    #             count += 1
    #             pre = cur
    #             cur = 0  # cur also serves as a flag
    #         elif s[i] != ' ':
    #             cur += 1
    #             pre = 0
    #     return pre if cur == 0 else cur


if __name__ == '__main__':
    """
    三个方法都要熟练掌握? 前两种即可
    方法1: split
        Note strip() start and end, lstrip() start, rstrip() end. 
        另外有个built reversed() 函数, 返回的是迭代器. 如果是generator, 速度应该可以?
        [::-1]不是迭代器, 需要copy一个new array
        另外"a " 应该return 1... trailing white space
    方法2: 从后往前.. 也可以把两个while合并.. 
    方法3: 记录前一个count, 并用cur count做flag...
    方法4: TODO 没理解 
        通用use "curr", "pre" from idea of Inorder traversal from TreeNode? 
    """
    s = Solution()
    print(s.lengthOfLastWord('  '))
    print(s.lengthOfLastWord('Hello World  c d   '))
    print(s.lengthOfLastWord('  b    a     '))

