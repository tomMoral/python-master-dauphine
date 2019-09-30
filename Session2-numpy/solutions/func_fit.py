# %%writefile solutions/func_fit.py

def fit(X, y):
    n_classes = len(np.unique(y))
    centroids = np.empty((n_classes, n_dim))
    for i in range(n_classes):
        centroids[i] = X[y == i].mean(axis=0)
    return centroids

centroids = fit(X_train, y_train)
plot_data(X_train, y_train, alpha=.2)
plot_data(centroids, range(2), s=256)

# %load solutions/func_fit.py
