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
            PRIMES.add(p*p)
PRIMES = set()
SieveOfEratosthenes(1000000)
n = int(input())
a = list(map(int, input().split()))
for i in a:
    if i in PRIMES:
        print('YES')
    else:
        print('NO')
         