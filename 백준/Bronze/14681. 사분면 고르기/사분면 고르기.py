x = [input() for i in range(2)]
x = tuple(map(lambda x: int(int(x)/abs(int(x))), x))

q = {(1, 1):1, (-1, 1):2, (-1, -1):3, (1, -1):4}
print(q[x])