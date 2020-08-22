import numpy as np

N= 100

# Vetor de ruído
x = 2*np.random.rand(N,1)

# Esperamos encontra algo próximo à y = 4 + 3
y =  4 + 3*x+np.random.randn(N,1)

X_b = np.c_[np.ones((N,1)),x]

# Implementação da esquação normal
a_optimum =  np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Best Solution
print(f'O valor ótimo de a0 é: {a_optimum[0][0]}')
print(f'O valor ótimo de a1 é: {a_optimum[1][0]}')