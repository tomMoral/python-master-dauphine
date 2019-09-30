# %%writefile solutions/exo04.py
# avec linspace, le début et la fin SONT inclus
# np.linspace?

# Créer un tableau avec les valeurs paires de 0 à 20:
l1 = np.linspace(0, 20, 11)
assert np.allclose(l1, x1)

# Créer un tableau avec les valeurs entre -1 et 1, tous les .1:
l2 = np.linspace(-1, .9, 20)
assert np.allclose(l2, x2)

# Créer un tableau avec les valeurs de 100 à 0:
l3 = np.linspace(100, 0, 101)
assert np.allclose(l3, x3)


# %load solutions/exo04.py
# # avec linspace, le début et la fin SONT inclus
# # np.linspace?

# # Créer un tableau avec les valeurs paires de 0 à 20:
# l1 =
# assert np.allclose(l1, x1)

# # Créer un tableau avec les valeurs entre -1 et 1, tous les .1:
# l2 =
# assert np.allclose(l2, x2)

# # Créer un tableau avec les valeurs de 100 à 0:
# l3 =
# assert np.allclose(l3, x3)
