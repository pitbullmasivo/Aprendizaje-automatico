import pandas as pd

# ventas CSV
ventas = pd.read_csv("ventas (1).csv")
print("Vista previa de ventas:")
print(ventas.head())

# clientes JSON
clientes = pd.read_json("clientes.json")
print("\nCantidad total de clientes:")
print(len(clientes))

# inventario Excel
inventario = pd.read_excel("inventario.xlsx")
promedio_stock = inventario["stock"].mean()

print("\nPromedio de stock disponible:")
print(promedio_stock)

ventas_combinadas = ventas.merge(
    inventario,
    left_on="producto",
    right_on="nombre",
    how="left"
)

print("\nDatos combinados de ventas e inventario:")
print(ventas_combinadas.head())