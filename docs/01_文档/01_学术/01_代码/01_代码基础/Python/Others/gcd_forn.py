import math;
import functools

T = int(input())
for _ in range (T):
    n = int(input())
    a = list(map(int,input().split()))
    gcd = functools.reduce(math.gcd,a)
    sqrt = math.ceil(math.sqrt(gcd))
    cd = [ x for x in range(1,sqrt) if gcd % x == 0]
    cd.extend([gcd // x for x in cd])
    if sqrt * sqrt == gcd: cd.append(sqrt)
    cd.sort()
    print(" ".join(list(map(str,cd)))) 