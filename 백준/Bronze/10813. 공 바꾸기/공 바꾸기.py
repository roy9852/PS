N, M = map(int, input().split())
x = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, input().split()) 
    i -= 1
    j -= 1
    
    temp = x[i]
    x[i] = x[j]
    x[j] = temp

for i in range(N):
    print(x[i], end = " ")
        