iter, goal = map(int, input().split())
coins = [int(input()) for _ in range(iter)]

n = 0
for i in range(iter-1, -1, -1):
    n += goal//coins[i]
    goal %= coins[i]

print(n)