# %%writefile solutions/exo07.py
t = np.linspace(0, 2 * np.pi, 1000)
x = np.cos(t)
y = np.sin(t)
ax = plt.subplot(aspect='equal')
ax.plot(x, y)
ax.vlines(0, -1, 1)
ax.hlines(0, -1, 1)

# %load solutions/exo07.py
