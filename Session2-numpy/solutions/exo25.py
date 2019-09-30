# %%writefile solutions/exo25.py

# t = np.linspace(-2, 6, 500)
XX, YY = np.meshgrid(t, t)

for i, mu_i in enumerate(mu):
    pdf = np.exp(-((XX - mu_i[0]) ** 2 + (YY - mu_i[1]) **2) / 2)
    plt.contour(XX, YY, pdf)

plot_data(mu, np.arange(2), s=256)

# %load solutions/exo25.py
