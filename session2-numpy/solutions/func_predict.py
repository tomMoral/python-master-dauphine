# %%writefile solutions/func_predict.py

def predict(X, centroids):
    C = cdist(X, centroids, 'sqeuclidean')
    y_pred = C.argmin(axis=-1)
    return y_pred

plot_data(X_test, y_test, alpha=.1)
wrong = y_test != y_pred
plot_data(X_test[wrong], y_pred[wrong])

# %load solutions/func_predict.py
