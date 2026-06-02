import math
import pandas as pd
import matplotlib.pyplot as plt


# =====================================
# Ecuación diferencial:
# y' = y
# y(0) = 1
# =====================================

def f(t, y):
    return y


def exact_solution(t):
    return math.exp(t)


# Parámetros
h = 0.2
t0 = 0
tf = 1
y0 = 1

# Euler
t_values = [t0]
y_euler = [y0]

t = t0
y = y0

while t < tf:
    y = y + h * f(t, y)
    t = round(t + h, 10)

    t_values.append(t)
    y_euler.append(y)

# Solución exacta
y_exact = [exact_solution(t) for t in t_values]

# Error absoluto
errors = [
    abs(exact - approx)
    for exact, approx in zip(y_exact, y_euler)
]

# Tabla de resultados
df = pd.DataFrame({
    "t": t_values,
    "Euler": y_euler,
    "Exacta": y_exact,
    "Error": errors
})

print("\nResultados:\n")
print(df)

# Guardar CSV
df.to_csv("results.csv", index=False)

# Gráfica
plt.figure(figsize=(8, 5))
plt.plot(t_values, y_exact, label="Solución exacta")
plt.plot(
    t_values,
    y_euler,
    "o--",
    label="Euler"
)

plt.title("Método de Euler vs Solución Exacta")
plt.xlabel("t")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("grafica.png")
plt.show()

# Error final
print("\nValor exacto en t=1:", y_exact[-1])
print("Valor Euler en t=1:", y_euler[-1])
print("Error:", errors[-1])