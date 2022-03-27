# -*- coding: utf-8 -*-
        
tcs = int(input())
for i in range(tcs):
    ln = int(input())
    st = list(map(int, input()))
    
    if sorted(st) == st:
        print(0)
    else:
        finalIndexes = []
        members = 0
        numZeros = st.count(0)
        numOnes = st.count(1)
        for i in range(numZeros):
            if(st[i] == 1):
                finalIndexes.append(i+1)
                members += 1
        for i in range(numZeros, ln):
            if(st[i] == 0):
                finalIndexes.append(i+1)
                members += 1
        print(1)
        print(members, *finalIndexes)
    