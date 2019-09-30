# %%writefile solutions/exo21.py
mu0 = np.zeros(n_dim)
mu1 = 3 * np.ones(n_dim)

print(mu0, mu1)

mu = np.concatenate([mu0[None], mu1[None]])
print(mu)

# %load solutions/exo21.py
