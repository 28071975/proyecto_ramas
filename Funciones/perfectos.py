# funciones/perfectos.py
# Realizado por Luis Fernando Valencia García

def es_perfecto(n):
    # Determinar si un número es perfecto
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma == n


def calcular_perfectos(minimo, maximo):
    # Retorna una lista con todos los números perfectos en el rango
    perfectos = []
    for num in range(minimo, maximo + 1):
        if es_perfecto(num):
            perfectos.append(num)
    return perfectos


# Programa principal con repetición
while True:
    print("\n=== BUSCADOR DE NÚMEROS PERFECTOS ===")

    minimo = int(input("Ingrese el número mínimo del rango: "))
    maximo = int(input("Ingrese el número máximo del rango: "))

    if minimo > maximo:
        print("El mínimo no puede ser mayor que el máximo. Inténtelo de nuevo.")
        continue

    resultado = calcular_perfectos(minimo, maximo)

    if resultado:
        print(f"Números perfectos entre {minimo} y {maximo}: {resultado}")
    else:
        print(f"No existen números perfectos entre {minimo} y {maximo}.")

    repetir = input("¿Desea ejecutar el programa nuevamente? (s/n): ").lower()
    if repetir != 's':
        print("Programa finalizado.")
        break