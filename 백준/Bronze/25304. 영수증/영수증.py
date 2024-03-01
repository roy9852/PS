X = int(input())
N = int(input())
bag = []
for i in range(N):
    price, number = map(int, input().split())
    X -= price*number

if X == 0:
    print("Yes")
else:
    print("No")
    