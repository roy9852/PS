test = int(input())
coins = [25, 10, 5, 1]

for iter in range(test):
    coin_list = []
    x = int(input())
    
    for coin in coins:
        coin_list.append(x//coin)
        x = x%coin
        
    for i in coin_list:
        print(i, end=" ")
    
    