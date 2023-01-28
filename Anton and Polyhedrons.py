import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n = int(input())    
    ans = 0
    for i in range(n):
        a = input()
        if a == "Tetrahedron":
            ans += 4
        elif a == "Cube":
            ans += 6
        elif a == "Octahedron":
            ans += 8
        elif a == "Dodecahedron":
            ans += 12
        elif a == "Icosahedron":
            ans += 20
    print(ans)

for _ in range(1):
    solve()