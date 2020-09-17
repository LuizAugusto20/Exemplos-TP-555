from sklearn.linear_model import LinearRegression
import numpy as np

N = 100
lin_reg = LinearRegression() # Instanciando
# Vetor de ruído
x = 2*np.random.rand(N,1)

# Esperamos encontra algo próximo à y = 4 + 3
y =  4 + 3*x+np.random.randn(N,1)

lin_reg.fit(x,y)

print(f'a0: {lin_reg.intercept_[0]}')
print(f'a0: {lin_reg.coef_[0][0]}')




