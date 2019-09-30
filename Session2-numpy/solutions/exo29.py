# %%writefile solutions/exo29.py

def predict(X, mu):
    C = ((X[:, None] - mu[None]) ** 2).sum(axis=-1)
    y_pred = C.argmin(axis=-1)
    return y_pred

y_pred = predict(X_test, mu)
plot_data(X_test, y_pred)

# %load solutions/exo29.py
