for _ in range(int(input())):
    n = int(input())
    s = input()
    if n ==1 or s[0] == s[1] or s[1] > s[0]:
        print(s[0]*2)
    else:
        a = [s[0]] 
        for i in range(1,n):
            if s[i] <= s[i-1]:
                a.append(s[i])
            else:
                break 
        print(''.join(j for j in a), end = '')
        print(''.join(j for j in reversed(a)))
        
    
    