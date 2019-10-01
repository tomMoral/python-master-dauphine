# %%writefile solutions/exo03.py
# Généré un tableau de 0 de taille 3, puis de taille (2, 3)
v0 = np.zeros(3)
M0 = np.zeros((2, 3))
print("0 vector of size: {}\n".format(v0.shape), v0)
print("0 matrix of size: {}\n".format(M0.shape), M0)
assert v0.shape == (3,)
assert M0.shape == (2, 3)
assert np.all(M0 == 0)

# Généré un tableau de 1 de taille 10, puis de taille 3x4x5
v1 = np.ones(10)
M1 = np.ones((2, 3, 2))
print("1 vector of size: {}\n".format(v1.shape), v1)
print("1 tensor of size: {}\n".format(M1.shape), M1)
assert v1.shape == (10,)
assert M1.shape == (2, 3, 2)
assert np.all(M1 == 1)

# Généré la matrice identité de taille 4x4
I = np.eye(4)
print("Id matrix of size: {}\n".format(I.shape), I)

# %load solutions/exo03.py
# # Généré un tableau de 0 de taille 3, puis de taille (2, 3)
# v0 =
# M0 =
# print("0 vector of size: {}\n".format(v0.shape), v0)
# print("0 matrix of size: {}\n".format(M0.shape), M0)
# assert v0.shape == (3,)
# assert M0.shape == (2, 3)
# assert np.all(M0 == 0)

# # Généré un tableau de 1 de taille 10, puis de taille 3x4x5
# v1 =
# M1 =
# print("1 vector of size: {}\n".format(v1.shape), v1)
# print("1 tensor of size: {}\n".format(M1.shape), M1)
# assert v1.shape == (10,)
# assert M1.shape == (2, 3, 2)
# assert np.all(M1 == 1)

# # Généré la matrice identité de taille 4x4
# I =
# print("Id matrix of size: {}\n".format(I.shape), I)
