# %%writefile solutions/exo10.py
X = np.random.randn(100, 5)
X -= X.mean(axis=0)
X /= X.std(axis=0)

print(X.mean(axis=0), X.std(axis=0))

%load solutions/exo10.py
