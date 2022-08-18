import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
def get(n):  
    x = 0
    for i in PRIMES:
        if i * i > n:
            break
        while n % i == 0:
            n //= i
            x += 1
    if n > 1:
        x += 1
    return x
 
def solve():
    a, b, k = map(int, input().split())    
    if k==1:
        if a!=b and (a%b==0 or b%a==0):
            print('YES')
        else:
            print('NO')
    else:
        mx = get(a) + get(b)
        if mx >= k:
            print('YES')
        else:
            print('NO')
            
def prime_range(n):
    sieve = [True] * n
    p = []
    for i in range(2, n):
        if sieve[i]:
            p.append(i)
            for j in range(i * i, n, i):
                sieve[j] = False
    return p
PRIMES = prime_range(int(10E5) + 1)
L = len(PRIMES)          
for _ in range(int(input())):
    solve()