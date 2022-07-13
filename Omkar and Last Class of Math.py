def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            PRIMES.add(p)

def solve():
    n = int(input())
    #a, b = map(int, input().split())    
    #a = list(map(str, input())) 
    
    if n % 2 == 0:
        print(n // 2, n // 2)
        return
    if n in PRIMES:
        print(n - 1, 1)
        return
    for i in PRIMES_LIST:
        if n % i == 0:
            print(n // i, n - n // i)
            return
    print(1, n - 1)
            
PRIMES = set() 
SieveOfEratosthenes(1000000) 
PRIMES_LIST = list(PRIMES)
for _ in range(int(input())):
    solve()

    