def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)
while True:
    try:
        a,b=map(int,raw_input().split())
        print(lcm(a,b))
    except:
        break