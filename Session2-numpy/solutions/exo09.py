# %%writefile solutions/exo09.py
A = np.array([[3, -2, 1], [1, 5, 10], [0, 1, -1]])
b = np.array([10, 21, -5])

x = np.linalg.inv(A) @ b
print(x)
x = [1, -2, 3]
print(A @ x)

# %load solutions/exo09.py
