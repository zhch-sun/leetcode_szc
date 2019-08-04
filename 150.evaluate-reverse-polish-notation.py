#
# @lc app=leetcode id=150 lang=python
#
# [150] Evaluate Reverse Polish Notation
#
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operator = set(['+', '-', '*', '/'])
        for item in tokens:
            if item not in operator:
                stack.append(int(item))
            else:
                a = stack.pop()
                b = stack.pop()
                if item == '+':
                    c = b + a
                elif item == '-':
                    c = b - a
                elif item == '*':
                    c = b * a
                elif item == '/':
                    c = int(float(b) / a)  # rounding towards zero...
                stack.append(c)
        return stack[-1]

        
if __name__ == '__main__':
    """
    注意除法要truncate to zero? 还有负数
    TODO https://stackoverflow.com/questions/19919387/in-python-what-is-a-good-way-to-round-towards-zero-in-integer-division
    还有个变种, 正常顺序但是加满括号. 算法第四版里面有个答案, 需要符号和操作数两个stack. 
    """
    s = Solution()
    # print(s.evalRPN(["2", "1", "+", "3", "*"]))
    # print(s.evalRPN(["4", "13", "5", "/", "+"]))
    print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
