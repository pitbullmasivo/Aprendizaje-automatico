import numpy as np

# Ejercicio 1
e1 = np.zeros(10)
print("Ejercicio 1:", e1)

# Ejercicio 2
e2 = np.arange(1, 21)
print("Ejercicio 2:", e2)

# Ejercicio 3
e3 = np.arange(2, 51, 2)
print("Ejercicio 3:", e3)

# (El ejercicio 3 está repetido, mismo resultado)

# Ejercicio 5
e5 = np.random.rand(4, 4)
print("Ejercicio 5:\n", e5)

# Ejercicio 6
a = np.array([1,2,3])
b = np.array([4,5,6])
e6 = a + b
print("Ejercicio 6:", e6)

# Ejercicio 7
m1 = np.random.randint(1, 11, (3,3))
m2 = np.random.randint(1, 11, (3,3))
e7 = np.dot(m1, m2)
print("Matriz 1:\n", m1)
print("Matriz 2:\n", m2)
print("Ejercicio 7 (multiplicación):\n", e7)

# Ejercicio 8
e8 = np.random.randint(1, 101, 15)
print("Ejercicio 8:", e8)
print("Máximo:", np.max(e8))
print("Mínimo:", np.min(e8))
print("Promedio:", np.mean(e8))

# Ejercicio 9
e9 = np.arange(1, 26).reshape(5,5)
diagonal = np.diag(e9)
print("Ejercicio 9:\n", e9)
print("Diagonal:", diagonal)

# Ejercicio 10
e10 = np.random.randint(1, 21, (5,5))
print("Ejercicio 10:\n", e10)
print("Suma por filas:", np.sum(e10, axis=1))
print("Suma por columnas:", np.sum(e10, axis=0))