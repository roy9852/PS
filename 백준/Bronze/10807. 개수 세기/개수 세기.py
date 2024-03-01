N = int(input())

# using dictionary
D = dict()
for i in map(int, input().split()):
    if i in D:
        D[i] += 1
    else :
        D[i] = 1
    
x = int(input())
print(0 if not(x in D) else D[x])