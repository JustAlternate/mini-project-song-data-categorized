import numpy as np
import matplotlib.pyplot as plt

categories = ['Rock', 'Heavy Metal', 'Power Metal', 'EDM', 'Techno']

# Our matrix categories-rules
M = np.array([
    [1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1]
])

# Transpose the matrix to focus on categories (columns) rather than rules (rows)
Mt = M.T

cov_matrix = np.cov(Mt, rowvar=False)

# --------------------
# THIS PAR OF THE CODE IS THANKS TO STARCODER2 :
eigen_values, eigen_vectors = np.linalg.eigh(cov_matrix)
sorted_index = np.argsort(eigen_values)[::-1]
sorted_eigenvalue = eigen_values[sorted_index]
sorted_eigenvectors = eigen_vectors[:, sorted_index]
eigenvector_subset = sorted_eigenvectors[:, 0:2]
# --------------------

final_pos = np.dot(Mt, eigenvector_subset)

plt.figure(figsize=(8, 6))
plt.scatter(final_pos[:, 0], final_pos[:, 1])

for i, category in enumerate(categories):
    plt.text(final_pos[i, 0], final_pos[i, 1], category, fontsize=12, ha='right')

plt.title("Clustering of categories using PCA")
plt.xlim(-3,2)
plt.ylim(-1,2)
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.tight_layout()
plt.show()
