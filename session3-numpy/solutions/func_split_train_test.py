# %%writefile solutions/func_split_train_test.py

def split_train_test(X, y, ratio=.5):
    n_points = len(X)
    id_shuffle = np.random.permutation(n_points)
    n_train = int(ratio * n_points)
    id_train, id_test = id_shuffle[:n_train], id_shuffle[n_train:]
    X_train, y_train = X[id_train], y[id_train]
    X_test, y_test = X[id_test], y[id_test]
    return (X_train, y_train), (X_test, y_test)

(X_train, y_train), (X_test, y_test) = split_train_test(X, y, .3)
print(X_train.shape, X_test.shape)

# %load solutions/func_split_train_test.py
