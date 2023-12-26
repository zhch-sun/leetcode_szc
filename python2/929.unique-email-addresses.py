#
# @lc app=leetcode id=929 lang=python
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        ans = set([])
        for s in emails:
            rs = ''
            split = s.split('@')
            first = split[0]
            for char in first:
                if char == '.':
                    continue
                elif char == '+':
                    break
                else:
                    rs += char
            rs += '@' + split[1]
            ans.add(rs)
        return len(ans)
        
if __name__ == '__main__':
    """
    
    """
    s = Solution()
    print(s.numUniqueEmails(["test.email+alex@leetcode.com",\
        "test.e.mail+bob.cathy@leetcode.com",\
            "testemail+david@lee.tcode.com"]))
# @lc code=end

