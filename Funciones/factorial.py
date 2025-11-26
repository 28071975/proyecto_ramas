# funciones/factorial.py
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

for i in range(1, 11):
    print(f"Factorial de {i} = {factorial(i)}")
