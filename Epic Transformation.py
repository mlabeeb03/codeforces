from queue import PriorityQueue
def solve():
    n = int(input())
    #n, W = map(int, input().split())    
    a = list(map(int, input().split())) 
    #a = list(map(str, input())) 
    
    dic = {}
    for i in a:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    v = list(dic.values())
    size = len(v)
    sz = n
    q = PriorityQueue()
    for i in v:
        q.put(i * -1)
    while size >= 2:
        a = -1 * q.get()
        b = -1 * q.get()
        a -= 1
        b -= 1
        sz -= 2
        if a > 0:
            q.put(a * -1)
        else:
            size -= 1
        if b > 0:
            q.put(b * -1)
        else:
            size -= 1
                   
    print(sz)
    
for _ in range(int(input())):
    solve()

    