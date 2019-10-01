# %%writefile solutions/exo26.py

mask_train = np.random.rand(n_points) > .5
X_train, y_train = X[mask_train], y[mask_train]
X_test, y_test = X[~mask_train], y[mask_train]
print(X_train.shape, X_test.shape)

# %load solutions/exo26
