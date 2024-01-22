x = [int(v) for v in input().split()]
y = [x.count(v) for v in x]
if max(y) == 3: print(10000+ 1000*x[y.index(3)])
elif max(y) == 2: print(1000+ 100*x[y.index(2)])    
else: print(100*max(x))