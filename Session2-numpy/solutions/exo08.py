# %%writefile solutions/exo08.py
M = np.random.randn(5, 6)
M[:, ::2] -= 2* M[:, 1::2]
M[M < 0] = 0

# %load solutions/exo08.py
