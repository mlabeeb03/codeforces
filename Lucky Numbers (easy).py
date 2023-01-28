import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
import itertools

def do(n, ln):
    if ln % 2 != 0:
        ln += 1
    stuff = None
    if ln % 2 != 0:
        ln += 1
    stuff = ([4] * (ln // 2)) + ([7] * (ln // 2))
    
    for L in range(len(stuff) + 1):
        for subset in itertools.permutations(stuff, ln):
            num = int(''.join(map(str, subset)))
            if num >= n:
                print(num)
                return 0
    return 1

def solve():
    n = input()
    ln = len(n)
    if do(int(n), ln) == 1:
        do(int(n),  ln + 2)
    
for _ in range(1):
    solve()
    