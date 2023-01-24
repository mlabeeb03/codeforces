from collections import OrderedDict, Counter

def solve():
    n = int(input())
    a = list(map(str, input()))
    dic = Counter(a)
    for i in range(1, 27):
        if chr(i + 96) not in dic:
            dic[chr(i + 96)] = 0
    odic = OrderedDict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    have = list(odic.keys())
    #print(odic)
    ans = n
    arr = [a[0]] * n
    for i in range(1, 27):
        if n % i == 0:
            avb = {}
            for j in range(i):
                avb[have[j]] = n // i
            #print(avb)
            novo = [None] * n
            for i in range(n):
                if a[i] in avb and avb[a[i]] > 0:
                    novo[i] = a[i]
                    avb[a[i]] -= 1
            rem = []
            for i in avb:
                if avb[i] > 0:
                    rem += [i] * avb[i]
            local = len(rem)
            if local < ans:
                for i in range(n):
                    if novo[i] is None:
                        novo[i] = rem.pop()
                ans = local
                arr = novo[:]
    print(ans)
    print(''.join(i for i in arr))

for _ in range(int(input())):
    solve()