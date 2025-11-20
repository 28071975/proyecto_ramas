# Autor: Oscar Mendez
# Función: calcular serie de Fibonacci
# Descripción: retorna la secuencia hasta n términos

def fibonacci(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n debe ser un entero positivo")

    secuencia = [0, 1]
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia[:n]
# funciones/fibonacci.py