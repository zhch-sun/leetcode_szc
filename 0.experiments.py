# -*- coding: utf-8 -*- 

# ---------------整数浮点数速度实验-------------# 
# 结论, 正常情况速度相同, 只在超出64bit之后有性能差距
# 1000个bit之后差距明显. 

# 加减法都在3ms左右
# ans = 0
# for _ in xrange(10000):
#     ans += 345
#     ans -= 344

# ans = 0.
# for _ in xrange(10000):
#     ans += 345.
#     ans -= 344.

# 整数乘除法30ms, 浮点数乘除法3ms
# ans = 1
# for _ in xrange(10000):
#     ans *= 600
#     ans /= 300

# ans = 1.
# for _ in xrange(10000):
#     ans *= 600
#     ans /= 300

# 保证范围都在64bit之内后都是3ms
# ans = 1
# for _ in xrange(10000):
#     ans *= 600
#     ans /= 600

# ans = 1.
# for _ in xrange(10000):
#     ans *= 600
#     ans /= 600

# 循环1000时 827us 527us
# ans = 1
# for _ in xrange(1000):
#     ans *= 600
#     ans /= 300

# ans = 1.
# for _ in xrange(1000):
#     ans *= 600
#     ans /= 300

# 一样的速度. 
# a = [6000000] * 10000
# b = [7000000] * 10000
# ans = 0
# for i, j in zip(a, b):
#     ans += i * j

# a = [6000000] * 10000
# b = [7000000] * 10000
# ans = 0.
# for i, j in zip(a, b):
#     ans += i * j