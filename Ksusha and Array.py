import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n = int(input())    
    s = list(map(int, input()))
    t = list(map(int, input()))
    dic = {'00': 0, '01': 0, '10': 0, '11': 0}
    for i in range(2 * n):
        dic[str(s[i]) + str(t[i])] += 1
        
    first = {0: 0, 1: 0}
    second = {0: 0, 1: 0}
    
    for i in range(n):
        if dic['11'] > 0:
            dic['11'] -= 1
            first[1] += 1
        elif dic['10'] > 0:
            dic['10'] -= 1
            first[1] += 1
        elif dic['01'] > 0:
            dic['01'] -= 1
            first[0] += 1
        else:
            dic['00'] -= 1
            first[0] += 1
            
        if dic['11'] > 0:
            dic['11'] -= 1
            second[1] += 1
        elif dic['01'] > 0:
            dic['01'] -= 1
            second[1] += 1
        elif dic['10'] > 0:
            dic['10'] -= 1
            second[0] += 1      
        else:
            dic['00'] -= 1
            second[0] += 1
            
    if first[1] > second[1]:
        print('First')
    elif first[1] < second[1]:
        print('Second')
    else:
        print('Draw')

for _ in range(1):
    solve()

    