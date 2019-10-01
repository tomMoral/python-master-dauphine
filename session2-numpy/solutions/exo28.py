# %%writefile solutions/exo28.py

n_classes = len(np.unique(y))
centroid = np.empty((n_classes, n_dim))
for i in range(n_classes):
    centroid[i] = X[y == i].mean(axis=0)

plot_data(X, y, alpha=.1)
plot_data(centroid, range(2), s=256)

# %load solutions/exo28.py
