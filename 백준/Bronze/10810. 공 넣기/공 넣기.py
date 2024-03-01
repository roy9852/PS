N, M = map(int, input().split())
x = [0]*N
for i in range(M):
    start, end, ball = map(int, input().split())
    start -= 1
    end -= 1
    
    for j in range(start, end+1):
        x[j] = ball

for i in range(N):        
    print(x[i], end = " ")