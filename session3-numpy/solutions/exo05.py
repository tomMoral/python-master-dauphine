# %%writefile solutions/exo05.py
E = np.zeros((8, 8))
E[0::2, 0::2] = 1
E[1::2, 1::2] = 1
plt.matshow(E, cmap='gray')


E = np.tile([[1, 0], [0, 1]], (4, 4))
E

np.tile?

# %load solutions/exo05.py
