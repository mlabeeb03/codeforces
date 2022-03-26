# -*- coding: utf-8 -*-

import math

def solve(s, t):
    slen, tlen = len(s), len(t)
    s *= tlen
    t *= slen
    lcm = int((slen * tlen) / math.gcd(slen, tlen))
    if(s != t):
        print(-1)
    else:
        print(s[:lcm])

tcs = int(input())
for i in range(tcs):
    s = input()
    t = input()
    solve(s, t)
    

    