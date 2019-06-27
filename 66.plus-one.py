#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#
class Solution(object):
    # def plusOne(self, digits):
    #     """
    #     :type digits: List[int]
    #     :rtype: List[int]
    #     """
    #     num = 0
    #     for d in digits:
    #         num = num * 10 + d  # Note this!
    #     return [int(i) for i in str(num+1)]
    
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + [0] * len(digits)
            

if __name__ == '__main__':
    """
    two solution. 
    1. for loop, note all the detail. 
    2. convert to string
    """
    s = Solution()
    print(s.plusOne([1,2,9]))
