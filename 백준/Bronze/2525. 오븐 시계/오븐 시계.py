H, M = map(int, input().split())
L = int(input())

T = H*60 + M + L
if T >= 24*60:
    T -= 24*60
    
H = T//60
M = T%60

print(f"{H} {M}")