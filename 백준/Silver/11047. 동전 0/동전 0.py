iter, goal = map(int, input().split())
coins = [int(input()) for _ in range(iter)]
coins.sort()
coins.reverse()

n = 0
for coin in coins:
    n += goal//coin
    goal = goal%coin

print(n)