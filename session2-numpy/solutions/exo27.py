# %%writefile solutions/exo27.py

id_shuffle = np.random.permutation(n_points)
id_train, id_test = id_shuffle[:500], id_shuffle[500:]
X_train, y_train = X[id_train], y[id_train]
X_test, y_test = X[id_test], y[id_test]
print(X_train.shape, X_test.shape)

# %load solutions/exo27
