# %%writefile solutions/func_generate_data.py

def generate_data(n_points, mu):
    n_classes, n_dim = mu.shape
    y = np.random.randint(n_classes, size=n_points)
    X = np.random.randn(n_points, n_dim)
    X += mu[y]
    return X, y

X, y = generate_data(n_points, mu)
print(X.shape, y.shape)

# %load solutions/func_generate_data.py
