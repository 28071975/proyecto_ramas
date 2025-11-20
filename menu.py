# menu.py
# Importa las funciones de los módulos de mis compañeros.

# menu.py

# Importación de las funciones desde el paquete 'funciones'.
# try:
   # from funciones.fibonacci import calcular_fibonacci
   # from funciones.factorial import calcular_factorial
   # from funciones.primos import es_primo
   # from funciones.perfectos import generar_perfectos
except ImportError as e:
    
    print(f"⚠️ Aviso: No se pudo importar un módulo de función. Asegúrese de que todos los archivos .py estén creados en 'funciones/'. Error: {e}")
    
    def calcular_fibonacci(n): return f"Función Fibonacci de {n} no implementada."
    def calcular_factorial(n): return f"Función Factorial de {n} no implementada."
    def es_primo(n): return f"Función Primos de {n} no implementada."
    def generar_perfectos(n): return f"Función Perfectos para {n} no implementada."


def mostrar_menu():
    """Muestra las opciones del menú."""
    print("\n" + "="*45)
    print("      *** MENÚ DE FUNCIONALIDADES MATEMÁTICAS *** ")
    print("="*45)
    print("1. 🔢 Cálculo de Serie Fibonacci")
    print("2. ❗ Cálculo Factorial de un Número")
    print("3. ✨ Determinar si un Número es Primo")
    print("4. 💎 Generar los N Primeros Números Perfectos")
    print("5. 🚪 Salir")
    print("="*45)

def ejecutar_opcion(opcion):
    """Ejecuta la funcionalidad seleccionada por el usuario, manejando la entrada."""
    try:
        if opcion == '1':
            print("\n--- 🔢 Cálculo de Serie Fibonacci ---")
            n = int(input("Ingrese el número de términos (N) a generar: "))
            resultado = calcular_fibonacci(n)
            print(f"Resultado: Serie Fibonacci de los primeros {n} términos: {resultado}")
            
        elif opcion == '2':
            print("\n--- ❗ Cálculo Factorial ---")
            n = int(input("Ingrese un número entero no negativo para calcular su factorial: "))
            resultado = calcular_factorial(n)
            print(f"Resultado: El factorial de {n} es: {resultado}")
            
        elif opcion == '3':
            print("\n--- ✨ Determinar si un Número es Primo ---")
            n = int(input("Ingrese un número entero para verificar si es primo: "))
            es_primo_resultado = es_primo(n)
            if es_primo_resultado is True:
                print(f"Resultado: El número {n} ES primo.")
            elif es_primo_resultado is False:
                print(f"Resultado: El número {n} NO es primo.")
            else:
                 # Mensaje para cuando aún no está implementada
                 print(f"Resultado: {es_primo_resultado}") 
            
        elif opcion == '4':
            print("\n--- 💎 Generar N Números Perfectos ---")
            n = int(input("Ingrese la cantidad (N) de números perfectos a encontrar: "))
            perfectos_encontrados = generar_perfectos(n)
            print(f"Resultado: Los primeros {n} números perfectos son: {perfectos_encontrados}")
            
        elif opcion == '5':
            print("👋 Saliendo del programa. ¡Hasta pronto!")
            return True # Indica que se debe salir del bucle
        
        else:
            print("❌ Opción no válida. Por favor, ingrese un número del 1 al 5.")

    except ValueError:
        print("❌ Error de entrada: Por favor, ingrese un número entero válido.")
    except Exception as e:
        # Captura cualquier error dentro de las funciones de tus compañeros
        print(f"❌ Ocurrió un error al ejecutar la función: {e}")
        
    return False # Indica que debe continuar en el bucle

def ejecutar_menu():
    """Bucle principal del menú que se ejecuta hasta que el usuario elige 'Salir'."""
    salir = False
    while not salir:
        mostrar_menu()
        opcion = input("▶️ Seleccione una opción (1-5): ").strip()
        salir = ejecutar_opcion(opcion)