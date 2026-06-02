# Solución de una Ecuación Diferencial mediante Separación de Variables y Método de Euler

## Objetivo

Resolver una ecuación diferencial ordinaria de forma analítica utilizando el método de separación de variables y aproximar la solución numéricamente mediante el método de Euler.

---

## Problema

Se considera la ecuación diferencial:

dy/dt = y

con la condición inicial:

y(0) = 1

y se desea aproximar la solución en el intervalo:

t ∈ [0,1]

utilizando un tamaño de paso:

h = 0.2

---

## Solución Analítica

La ecuación es separable:

dy/y = dt

Integrando ambos lados:

ln|y| = t + C

Despejando:

y = Ce^t

Aplicando la condición inicial:

1 = Ce^0

C = 1

Por lo tanto, la solución exacta es:

y(t) = e^t

---

## Método de Euler

La fórmula utilizada es:

y_(n+1) = y_n + h*f(t_n,y_n)

donde:

f(t,y) = y

Se utiliza:

- h = 0.2
- y(0) = 1

---

## Resultados

| t | Euler |
|---|--------|
|0.0|1.000000|
|0.2|1.200000|
|0.4|1.440000|
|0.6|1.728000|
|0.8|2.073600|
|1.0|2.488320|

Valor exacto:

e = 2.718282

Valor aproximado por Euler:

2.488320

Error:

0.229962

---

## Ejecución

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar:

```bash
python main.py
```

---

## Archivos generados

- results.csv → tabla de resultados.
- grafica.png → comparación entre la solución exacta y Euler.

---

## Instalación y Ejecución

## 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/ecuacion-diferencial-euler.git
```

Entrar al directorio:

```bash
cd ecuacion-diferencial-euler
```

---

## 2. Crear un entorno virtual (opcional pero recomendado)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Ejecutar el programa

```bash
python main.py
```

---

## 5. Resultados esperados

Al ejecutar el programa se mostrarán:

- La tabla de aproximaciones de Euler.
- La solución exacta.
- El error absoluto en cada punto.
- Una gráfica comparando ambas soluciones.

Además se generarán los archivos:

```text
results.csv
grafica.png
```

---

## Requisitos

- Python 3.10 o superior
- pip

Verificar versión instalada:

```bash
python --version
```