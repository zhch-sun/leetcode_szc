# import sys 
# for line in sys.stdin:
#     a = line.split()
#     print int(a[0]) + int(a[1])


# # using monotonic stack
# while True:
#     try:
#         numStr = raw_input().strip()
#         nums = map(int, list(numStr))
#         # record last position of nums
#         memo = {}  
#         for i, n in enumerate(nums):
#             memo[n] = i 
#         # monotonic stack
#         sta = []
#         for i, n in enumerate(nums):
#             if n in sta:  # can be better with binary search
#                 continue
#             while sta and (sta[-1] < n and memo[sta[-1]] > i):
#                 sta.pop()                
#             sta.append(n)
#         print ''.join(map(str, sta))
#     except:
#         break

class Node(object):
    def __init__(self, name):
        self.name = name
        self.next = None
        self.isCycle = False
        self.used = False

def cycle_det(node):
    if node.used:
        return
    node.used = True
    slow = fast = node
    while fast and fast.next:
        # if fast.isCycle or fast.next.isCycle:
        #     return
        fast.used = True
        fast.next.used = True
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            fast.isCycle = True
            fast = fast.next
            while fast is not slow:
                fast.isCycle = True
                fast = fast.next
            break
    return 

try:
    memo = {}
    while True:
        line = raw_input()
        if line[-1] == ',':
            line = line[:-1]
        n1, n2 = line[1:-1].split(',')
        n1, n2 = n1.strip(), n2.strip()
        if n1 not in memo:
            memo[n1] = Node(n1)
        if n2 not in memo:
            memo[n2] = Node(n2)
        memo[n1].next = memo[n2]     
except:
    for _, node in memo.items():
        cycle_det(node)
    pairs = list(memo.items())
    pairs.sort(key=lambda x: int(x[0][2:]))
    N = len(pairs)
    for i, (a, b) in enumerate(pairs):
        ans = '{' + a + ', '
        ans += 'true}' if b.isCycle else 'false}'
        ans += ',' if i != N - 1 else ''
        print ans
