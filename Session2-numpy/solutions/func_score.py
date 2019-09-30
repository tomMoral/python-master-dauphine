# %%writefile  solutions/func_score.py
def score(y_pred, y_true):
    return np.mean(y_pred == y_true)

print("Accuracy of our model: {:7.2%}"
      .format(accuracy(y_test, y_pred)))

# %load solutions/func_score.py
