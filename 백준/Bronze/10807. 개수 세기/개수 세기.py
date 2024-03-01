N = int(input())

# using list
L = list(map(int, input().split()))
x = int(input())

cnt = 0
for i in range(N):
    if x == L[i]:
        cnt += 1

print(cnt)