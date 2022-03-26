# -*- coding: utf-8 -*-

def lastIndex(arr, x):
    for i in reversed(range(len(arr))):
        if(arr[i] == x):
            return i
        
def solve(n, exp):
    if exp.count(2) in range(1,3):
        print('NO')
        return
    else:
        board = [['=' for i in range(n)]for i in range(n)]
        for i in range(n):
            board[i][i] = 'X'
        if exp.count(2) != 0:
            
            firstIndexOf2 = exp.index(2)
            lastIndexOf2 = lastIndex(exp, 2)
            for i in range(firstIndexOf2, lastIndexOf2):
                if(exp[i] == 2):
                    for j in range(i+1, lastIndexOf2 + 1):
                        if(exp[j] == 2):
                            board[i][j] = '+'
                            board[j][i] = '-'
            board[lastIndexOf2][firstIndexOf2] = '+'
            board[firstIndexOf2][lastIndexOf2] = '-'
                
        print('YES')
        for i in range(n):
            print(''.join(board[i]))

tcs = int(input())
for i in range(tcs):
    n = int(input())
    e = input()
    exp = list(map(int, e))
    solve(n, exp)
    

    