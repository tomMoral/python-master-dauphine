pi = 2
for i in range(1, 1000):
    pi *= (4*i*i) / (4*i**2 - 1)
print(pi)